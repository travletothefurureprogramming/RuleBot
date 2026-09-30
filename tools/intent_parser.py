import json
import random
import sys
from pathlib import Path

PARENT_DIR = Path(__file__).resolve().parent.parent
if str(PARENT_DIR) not in sys.path:
    sys.path.append(str(PARENT_DIR))

from tools import text_cleaner, time, weather

JSON_PATH = PARENT_DIR / "data" / "intent.json"


def load_intents(file_path=JSON_PATH):
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)


def find_intent_contains(user_input, intents_data=None):
    if intents_data is None:
        intents_data = load_intents()

    user_input = text_cleaner.clean_input(user_input)

    for intent in intents_data["intents"]:
        for pattern in intent["patterns"]:
            clean_pattern = text_cleaner.clean_input(pattern)
            if clean_pattern in user_input:
                return intent["responses"]

    return ["Δεν κατάλαβα τι εννοείς."]


def get_response(user_input):
    responses = find_intent_contains(user_input)

    selected_response = random.choice(responses)

    if selected_response == "weather":
        return f"Η τωρινή θερμοκρασία είναι: {weather.get_weather()}°F"
    elif selected_response == "time":
        return f"Η τωρινή ημερομηνία και ώρα είναι: {time.get_datetime()}"

    return selected_response


if __name__ == "__main__":
    print(get_response("καιρος"))