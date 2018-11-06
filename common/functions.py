
import os
from datetime import date

VERIFICATION_TOKEN = os.getenv('VERIFICATION_TOKEN', 'sesame')


def say(response, image_url=None):
    payload = {"attachments": [{"pretext": response}]}
    if image_url is not None:
        payload["attachments"][0]["image_url"] = image_url
    return payload


def valid(req):
    # TODO: Switch to secrets
    return req.form['token'] == VERIFICATION_TOKEN


def russ_travel():
    d0 = date.today()
    d1 = date(2019, 6, 13)
    delta = d1 - d0
    if delta.days > 0:
        return say(
            f'{delta.days} days until Russ moves back!',
            'https://media.giphy.com/media/xULW8poAH4m1KBQr1C/giphy.gif'
        )
    else:
        return say(
            'Russ is already back!',
            'https://media.giphy.com/media/xUOxeRRkTYdQJfyy2Y/giphy.gif'
        )
