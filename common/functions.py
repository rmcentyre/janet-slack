
import os
import time
import hashlib
import hmac

CLIENT_ID = os.getenv('CLIENT_ID', 'sesame')
CLIENT_SECRET = os.getenv('CLIENT_SECRET', 'sesame')
SIGNING_SECRET = os.getenv('SIGNING_SECRET', 'sesame')
VERIFICATION_TOKEN = os.getenv('VERIFICATION_TOKEN', 'sesame')
PRODUCTION = os.getenv('PRODUCTION', 'false')


def say(response, image_url=None):
    payload = {"attachments": [{"pretext": response}]}
    if image_url is not None:
        payload["attachments"][0]["image_url"] = image_url
    return payload


def valid(request):
    # Skip in staging
    if PRODUCTION == 'false':
        print("Slack request validation skipped!")
        return True
    else:
        # Extract the components from the request
        slack_signature = request.headers['X-Slack-Signature']
        timestamp = request.headers['X-Slack-Request-Timestamp']
        body = request.get_data()

        slack_request_validation(slack_signature, timestamp, body)


# Adapted from https://janikarhunen.fi/verify-slack-requests-in-aws-lambda-and-python
def compute_signature(timestamp, body):
    # create the basestring from the timestamp and body
    basestring = f"v0:{timestamp}:{body}".encode('utf-8')
    signing_secret = bytes(SIGNING_SECRET, 'utf-8')

    # create the signature from the signing secret and basestring
    signature = 'v0=' + hmac.new(signing_secret, basestring, hashlib.sha256).hexdigest()
    return signature


def slack_request_validation(slack_signature, timestamp, body, enforce_timestamp=True):
    if abs(int(time.time()) - int(timestamp)) > 60 * 5 and enforce_timestamp:
        print("Slack request validation failure!")
        print("Timestamp mismatch detected.")
        return False

    my_signature = compute_signature(timestamp, body)

    if hmac.compare_digest(my_signature, slack_signature):
        print("Slack request validation success!")
        return True
    else:
        print("Slack request validation failure!")
        print(f"Computed: [{my_signature}]")
        print(f"Expected: [{slack_signature}]")
        return False


def bad():
    say(
        "Nope.",
        "https://66.media.tumblr.com/868e5b2061c69445f2f634c51a2764f8/"
        "tumblr_p36zgwY6oS1virtjeo3_250.gif"
    )
