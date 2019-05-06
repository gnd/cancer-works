""" Speech to Text """

from __future__ import division

import time
import re
import sys

from google.cloud import speech

import pyaudio
from six.moves import queue

# Audio recording parameters
STREAMING_LIMIT = 55000
SAMPLE_RATE = 16000
CHUNK_SIZE = int(SAMPLE_RATE / 10)  # 100ms

class Orthograph():
    def __init__(self, lang='cs-CZ', exit_key='ananas', next_key='figaro'):
        self.client = speech.SpeechClient()
        self.config = speech.types.RecognitionConfig(
            encoding=speech.enums.RecognitionConfig.AudioEncoding.LINEAR16,
            sample_rate_hertz=SAMPLE_RATE,
            language_code=lang,
            max_alternatives=1,
            enable_word_time_offsets=True)
        self.streaming_config = speech.types.StreamingRecognitionConfig(
            config=self.config,
            interim_results=True)
        self.mic_manager = ResumableMicrophoneStream(SAMPLE_RATE, CHUNK_SIZE)
        self.exit_key = exit_key
        self.next_key = next_key

    def spell(self):
        """
            Returns:
                A list of transcription strings.
        """
        results = []
        with self.mic_manager as stream:
            while not stream.closed:
                audio_generator = stream.generator()
                requests = (speech.types.StreamingRecognizeRequest(
                    audio_content=content)
                    for content in audio_generator)

                responses = self.client.streaming_recognize(self.streaming_config,
                                                       requests)
                # Now, put the transcription responses to use.
                res = self._listen_print_loop(responses, stream)
                if res:
                    results.extend(res)
                else:
                    results = None
        return results

    def _listen_print_loop(self, responses, stream):
        results = []

        responses = (r for r in responses if (
                r.results and r.results[0].alternatives))

        for response in responses:
            if not response.results:
                continue

            # The `results` list is consecutive. For streaming, we only care about
            # the first result being considered, since once it's `is_final`, it
            # moves on to considering the next utterance.
            result = response.results[0]
            if not result.alternatives:
                continue

            # Display the transcription of the top alternative.
            top_alternative = result.alternatives[0]
            transcript = top_alternative.transcript

            if result.is_final:
                # result is final
                print(transcript)
                # Exit recognition if any of the transcribed phrases could be
                # one of our keywords.
                if re.search(r'\b({})\b'.format(self.exit_key), transcript, re.I):
                    print('Recognized %s. Exiting..' % self.exit_key)
                    stream.closed = True
                    results = None
                    break
                elif re.search(r'\b({})\b'.format(self.next_key), transcript, re.I):
                    print('Recognized %s. Moving on...' % self.next_key)
                    stream.closed = True
                    break
                else:
                    results.append(transcript)
        return results

def get_current_time():
    return int(round(time.time() * 1000))


def duration_to_secs(duration):
    return duration.seconds + (duration.nanos / float(1e9))


class ResumableMicrophoneStream:
    """Opens a recording stream as a generator yielding the audio chunks."""
    def __init__(self, rate, chunk_size):
        self._rate = rate
        self._chunk_size = chunk_size
        self._num_channels = 1
        self._max_replay_secs = 5

        # Create a thread-safe buffer of audio data
        self._buff = queue.Queue()
        self.closed = True
        self.start_time = get_current_time()

        # 2 bytes in 16 bit samples
        self._bytes_per_sample = 2 * self._num_channels
        self._bytes_per_second = self._rate * self._bytes_per_sample

        self._bytes_per_chunk = (self._chunk_size * self._bytes_per_sample)
        self._chunks_per_second = (
                self._bytes_per_second // self._bytes_per_chunk)

    def __enter__(self):
        self.closed = False

        self._audio_interface = pyaudio.PyAudio()
        self._audio_stream = self._audio_interface.open(
            format=pyaudio.paInt16,
            channels=self._num_channels,
            rate=self._rate,
            input=True,
            frames_per_buffer=self._chunk_size,
            # Run the audio stream asynchronously to fill the buffer object.
            # This is necessary so that the input device's buffer doesn't
            # overflow while the calling thread makes network requests, etc.
            stream_callback=self._fill_buffer,
        )

        return self

    def __exit__(self, type, value, traceback):
        self._audio_stream.stop_stream()
        self._audio_stream.close()
        self.closed = True
        # Signal the generator to terminate so that the client's
        # streaming_recognize method will not block the process termination.
        self._buff.put(None)
        self._audio_interface.terminate()

    def _fill_buffer(self, in_data, *args, **kwargs):
        """Continuously collect data from the audio stream, into the buffer."""
        self._buff.put(in_data)
        return None, pyaudio.paContinue

    def generator(self):
        while not self.closed:
            if get_current_time() - self.start_time > STREAMING_LIMIT:
                self.start_time = get_current_time()
                break
            # Use a blocking get() to ensure there's at least one chunk of
            # data, and stop iteration if the chunk is None, indicating the
            # end of the audio stream.
            chunk = self._buff.get()
            if chunk is None:
                return
            data = [chunk]

            # Now consume whatever other data's still buffered.
            while True:
                try:
                    chunk = self._buff.get(block=False)
                    if chunk is None:
                        return
                    data.append(chunk)
                except queue.Empty:
                    break

            yield b''.join(data)
