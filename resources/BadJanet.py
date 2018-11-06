from flask_restful import Resource
from flask import request

from common.functions import valid, say


class BadJanet(Resource):
    def post(self):
        if valid(request):
            return say(
                "'sup, _dinks_",
                "https://78.media.tumblr.com/8751842a9a7ba74524cb06e498ca6c1d/"
                "tumblr_ok25wy412i1udh64ho4_500.gif"
            )
