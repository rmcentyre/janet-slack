
from . import Janet
from common.functions import say


class BadJanet(Janet):

    responses = {
        # nothing yet
    }

    default_response = say(
        "'sup, _dinks_",
        "https://78.media.tumblr.com/8751842a9a7ba74524cb06e498ca6c1d/"
        "tumblr_ok25wy412i1udh64ho4_500.gif"
    )
