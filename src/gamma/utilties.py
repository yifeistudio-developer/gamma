import json
import logging

log = logging.getLogger(__name__)

def to_obj(str):
    try:
        return json.loads(str)
    except Exception as e:
        log.error('catch exception: %s', e)
        return {}