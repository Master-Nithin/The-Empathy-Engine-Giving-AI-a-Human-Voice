import json
from datetime import datetime

class Logger:

    def log(self, text, emotion, confidence):

        data = {
            "text": text,
            "emotion": emotion,
            "confidence": confidence,
            "time": str(datetime.now())
        }

        try:
            with open("history.json","r") as f:
                logs = json.load(f)
        except:
            logs = []

        logs.append(data)

        with open("history.json","w") as f:
            json.dump(logs,f,indent=4)