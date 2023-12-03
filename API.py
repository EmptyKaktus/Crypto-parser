import json


def api():
    with open("key.json") as f:
        templates = json.load(f)
    return templates[0]["API"]
