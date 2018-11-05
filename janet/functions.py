import os
from flask import jsonify

VERIFICATION_TOKEN = os.getenv('VERIFICATION_TOKEN', 'sesame')


def say(response, image_url=None):
    payload = {"attachments": [{"pretext": response}]}
    if image_url is not None:
        payload["attachments"][0]["image_url"] = image_url
    json = jsonify(payload)
    return json


def valid(req):
    return req.form['token'] == VERIFICATION_TOKEN
