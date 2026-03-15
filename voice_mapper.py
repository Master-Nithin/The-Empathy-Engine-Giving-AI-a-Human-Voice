import random

class VoiceMapper:

    def map_voice(self, emotion, intensity):

        params = {
            "rate": 1.0,
            "gender": "male"
        }

        if emotion == "joy":
            params["rate"] = 1.05
            params["gender"] = random.choice(["male","female"])

        elif emotion == "anger":
            params["rate"] = 1.1
            params["gender"] = "male"

        elif emotion == "sadness":
            params["rate"] = 0.9
            params["gender"] = "female"

        elif emotion == "surprise":
            params["rate"] = 1.05
            params["gender"] = random.choice(["male","female"])

        elif emotion == "fear":
            params["rate"] = 0.95
            params["gender"] = "female"

        else:
            params["rate"] = 1.0
            params["gender"] = random.choice(["male","female"])

        return params