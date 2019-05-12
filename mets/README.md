### mets (Metastasis)
---
#### Setup

1. `apt-get install portaudio19-dev`
2. `pip3 install -r requirements.txt`
3. Make sure you have a speech engine driver installed (e.g. by `apt-get install espeak`).
4. Set authentication for Google Cloud (e.g. `export GOOGLE_APPLICATION_CERTIFICATE=<path/to/certificate.json>` or [any other possible way](https://cloud.google.com/docs/authentication/production)).
5. Run `python3 poc.py  <args>`

#### Running

Atm, `poc.py` consists of a loop - you may speak, and what you say is transcribed through GC's Speech API into text, until a keyword is not recognized. At this point, the connection to GC is closed and the transcribed text (except the keyword) is forwarded to the running char-rnn language model. The generated text from the language model is spoken through a text-to-speech interface.
To exit the application, besides `Ctrl-C`-ing it, you can say the special killing keyword.


#### Notes

`poc.py` accepts the following optional arguments:
* The move-on-keyword is set by `--next_key <k>` and defaults to *figaro*.
* The exit-keyword is set by `--exit_key <k>` and defaults to *ananas*.
* The TTS and STT language is set by `--lang <l>` and defaults to `cs-CZ` (`en-US` works too).
* The directory containing a pretrained char-rnn model is set by `--char_rnn_ckpt_dir <d>` and defaults to `charrnn/save` (which by default doesn't exist, so make sure you either provide it or specify a valid path).
* After setting the patience flag with `--patient True`, the program will wait for you to hit Enter, before making new connections to the Speech API.
* By default, the text spoken includes the primed text (the transcription) and the generated text. To say only what has been generated, set `--say_primed False`.

You may like to choose the keywords based on the language used.

Make sure, that the speech transcriptions are in a character set, which belongs to the char-rnn model's vocabulary.