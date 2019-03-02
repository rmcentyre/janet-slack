
from . import Janet
from common.functions import say
from datetime import date


def russ_travel():
    d0 = date.today()
    d1 = date(2019, 7, 1)
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


class GoodJanet(Janet):

    responses = {
        'atl': russ_travel()
    }

    default_response = say(
        "Hi, there!",
        "http://78.media.tumblr.com/daf862b49b82e49a47354b14c5143363/"
        "tumblr_oefwev7pLA1vvi3bvo8_250.gif"
    )
