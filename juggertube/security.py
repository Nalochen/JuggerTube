from hmac import compare_digest
import functools

from flask import request

from juggertube.models import Device


def is_valid(api_key):
    device = Device.find_by_device_key(api_key)
    if device and compare_digest(device.device_key, api_key):
        return True


def api_required(func):
    @functools.wraps(func)
    def decorator(*args, **kwargs):
        print('hello')
        if request.json:
            api_key = request.json.get('api_key')
        else:
            return {'message': 'Please provide an API key'}, 400

        if is_valid(api_key):
            return func(*args, **kwargs)
        else:
            return {'message': 'The provided API key is not valid'}, 403
    return decorator
