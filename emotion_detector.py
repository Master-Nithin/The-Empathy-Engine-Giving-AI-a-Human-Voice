from transformers import pipeline

class EmotionDetector:

    def __init__(self):

        self.classifier = pipeline(
            "text-classification",
            model="j-hartmann/emotion-english-distilroberta-base",
            top_k=1
        )

    def detect(self, text):

        result = self.classifier(text)[0][0]

        emotion = result["label"]
        confidence = float(result["score"])

        return emotion, confidence