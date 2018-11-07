from flask_restful import Resource
from flask import request
from common.functions import valid, say, russ_travel


class Janet(Resource):
    def post(self):
        if valid(request):
            text = request.form.get('text', 'none')
            if text.lower() == 'atl':
                response = russ_travel()
            else:
                response = say(
                    "Hi, there!",
                    "http://78.media.tumblr.com/daf862b49b82e49a47354b14c5143363/"
                    "tumblr_oefwev7pLA1vvi3bvo8_250.gif"
                )
            return response
