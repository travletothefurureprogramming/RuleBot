from pathlib import Path
import sys

PARENT_DIR = Path(__file__).resolve().parent.parent
if str(PARENT_DIR) not in sys.path:
    sys.path.append(str(PARENT_DIR))

import json
from tools import text_cleaner, time, weather
import random

JSON_PATH = PARENT_DIR / "data" / "intent.json"


def load_intents(file_path=JSON_PATH):
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)

def find_intent_contains(user_input, intents_data=load_intents()):
    user_input = text_cleaner.clean_input(user_input)

    for intent in intents_data["intents"]:
        for pattern in intent["patterns"]:
            if pattern.lower() in user_input:
                if intent["responses"] == ["weather"]:
                    return f"Η τωρινη θερμοκρασία ειναι: {weather.get_weather()}"
                elif intent["responses"] == ["time"]:
                    return f"Η τωρινη ημερομηνία και ώρα ειναι: {time.get_datetime()}"
                else:
                    return intent["responses"]
            
    return "unknown"

def get_response(user_input):
    return random.choice(find_intent_contains(user_input))


if __name__ == "__main__":
    print(get_response("Γειά!"))
