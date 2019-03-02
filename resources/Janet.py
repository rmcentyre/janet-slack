
from flask_restful import Resource
from flask import request
from common.functions import valid, say, bad


class Janet(Resource):

    responses = {}

    default_response = say(
        "Neutral greeting.",
        "https://vignette.wikia.nocookie.net/thegoodplace/images/6/6a/Neutral_Janet.png"
        "/revision/latest/scale-to-width-down/240"
    )

    @classmethod
    def respond_to(cls, text):
        return cls.responses.get(text, cls.default_response)

    @classmethod
    def post(cls):
        if valid(request):
            text = request.form.get('text', 'none').lower()
            return cls.respond_to(text)
        else:
            return bad()
