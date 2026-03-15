import pyttsx3
import os

engine = pyttsx3.init()

def generate_voice(text, rate, volume):

    engine.setProperty("rate", rate)
    engine.setProperty("volume", volume)

    # Select male voice if available
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)   # usually male voice

    # create output folder if not present
    if not os.path.exists("output"):
        os.makedirs("output")

    file_path = "output/empathy_voice.wav"

    # Save audio file
    engine.save_to_file(text, file_path)

    # Speak the text
    engine.say(text)

    engine.runAndWait()

    return file_path