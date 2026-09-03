import json


def to_obj(str):
    try:
        return json.loads(str)
    except Exception:
        return {}