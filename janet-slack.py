
from flask import Flask, jsonify, request
import os
import dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
dotenv.load_dotenv(dotenv_path)

VERIFICATION_TOKEN = os.environ['VERIFICATION_TOKEN']

app = Flask(__name__)


def valid(request):
    return request.form['token'] == VERIFICATION_TOKEN


def say(response, image_url=None):
    payload = {"attachments": [{"pretext": response}]}
    if image_url is not None:
        payload["attachments"][0]["image_url"] = image_url
    json = jsonify(payload)
    return json


@app.route("/")
def no_humans():
    return "Warning: Not for human consumption!"


@app.route("/bot/hello", methods=['POST'])
def hello_world():
    if valid(request):
        return say("Hello, world!")


@app.route("/bot/janet", methods=['POST'])
def janet():
    if valid(request):
        return say("Hi, there!", "http://78.media.tumblr.com/daf862b49b82e49a47354b14c5143363/tumblr_oefwev7pLA1vvi3bvo8_250.gif")


@app.route("/bot/badjanet", methods=['POST'])
def hello_dinks():
    if valid(request):
        return say("'sup, _dinks_", "https://78.media.tumblr.com/8751842a9a7ba74524cb06e498ca6c1d/tumblr_ok25wy412i1udh64ho4_500.gif")


if __name__ == "__main__":
    app.run()
