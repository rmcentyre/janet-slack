
import os
from datetime import date

import dotenv
from flask import Flask, request

from janet.functions import say, valid

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
dotenv.load_dotenv(dotenv_path)

app = Flask(__name__)


@app.route("/bot/janet", methods=['POST'])
def janet():
    if valid(request):
        return say(
            "Hi, there!",
            "http://78.media.tumblr.com/daf862b49b82e49a47354b14c5143363/"
            "tumblr_oefwev7pLA1vvi3bvo8_250.gif"
        )


@app.route("/bot/badjanet", methods=['POST'])
def hello_dinks():
    if valid(request):
        return say(
            "'sup, _dinks_",
            "https://78.media.tumblr.com/8751842a9a7ba74524cb06e498ca6c1d/"
            "tumblr_ok25wy412i1udh64ho4_500.gif"
        )


@app.route("/bot/atl", methods=['POST'])
def russ_travel():
    if valid(request):
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


if __name__ == "__main__":
    app.run()
