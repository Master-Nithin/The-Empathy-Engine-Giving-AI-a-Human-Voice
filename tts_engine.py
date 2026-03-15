import pyttsx3
import re

class TTSEngine:

    def __init__(self):

        self.engine = pyttsx3.init()

        self.voices = self.engine.getProperty("voices")

    def select_voice(self, gender):

        if gender == "female" and len(self.voices) > 1:
            self.engine.setProperty("voice", self.voices[1].id)
        else:
            self.engine.setProperty("voice", self.voices[0].id)

    def set_rate(self, rate):

        base_rate = 160

        self.engine.setProperty("rate", int(base_rate * rate))

    def split_sentences(self, text):

        sentences = re.split(r'[.!?]', text)

        return [s.strip() for s in sentences if s.strip()]

    def speak(self, text):

        sentences = self.split_sentences(text)

        for sentence in sentences:
            self.engine.say(sentence)

        self.engine.runAndWait()