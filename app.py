from flask import Flask, render_template, request
from emotion_detector import EmotionDetector
from voice_mapper import VoiceMapper
from tts_engine import TTSEngine
from logger import InteractionLogger

app = Flask(__name__)

detector = EmotionDetector()
mapper = VoiceMapper()
tts = TTSEngine()
logger = InteractionLogger()


@app.route("/", methods=["GET", "POST"])
def index():

    emotion = None
    confidence = None
    audio_file = None
    params = None

    if request.method == "POST":

        text = request.form["text"]

        emotion, confidence = detector.detect(text)

        params = mapper.map_parameters(emotion, confidence)

        audio_file = tts.generate(text)

        logger.log(text, emotion, confidence)

    return render_template(
        "index.html",
        emotion=emotion,
        confidence=confidence,
        audio_file=audio_file,
        params=params
    )


if __name__ == "__main__":
    app.run(debug=True)