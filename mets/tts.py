""" Text to Speech """

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