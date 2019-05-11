""" Text to Speech """

import fire
import pyttsx3

class Voice():
    def __init__(self):
        pass

    def speak(self, str):
        pass

class DummyVoice(Voice):
    def __init__(self, lang='cs-CZ', rate=100):
        """
            Args:
                lang: cs-CZ or en-US
                rate: words per minute
        """
        self._engine = pyttsx3.init()
        if lang == 'cs-CZ':
            self._engine.setProperty('voice', 'czech')
        elif lang == 'en-US':
            self._engine.setProperty('voice', 'english')
        self._engine.setProperty('rate', rate)

    def speak(self, str):
        self._engine.say(str)
        self._engine.runAndWait()


def _main(lang='cs-CZ', rate=100):
    voice = DummyVoice(lang=lang, rate=rate)
    while True:
        voice.speak(input('>>> '))


if __name__ == "__main__":
    fire.Fire(_main)