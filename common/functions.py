
import os
import hmac

VERIFICATION_TOKEN = os.getenv('VERIFICATION_TOKEN', 'sesame')
SLACK_SIGNING_SECRET = os.getenv('SLACK_SIGNING_SECRET', 'sesame')


def say(response, image_url=None):
    payload = {"attachments": [{"pretext": response}]}
    if image_url is not None:
        payload["attachments"][0]["image_url"] = image_url
    return payload


def valid(request):
    # Extract the components from the request
    slack_signature = request.headers['X-Slack-Signature']
    request_timestamp = request.headers['X-Slack-Request-Timestamp']
    request_body = request.body()

    # create the basestring from two components
    basestring = f"v0:{request_timestamp}:{request_body}"

    # create the signature
    my_signature = 'v0=' + hmac.compute_hash_sha256(SLACK_SIGNING_SECRET, basestring).hexdigest()

    if hmac.compare(my_signature, slack_signature):
        return True
    else:
        return False


def bad():
    say(
        "Nope.",
        "https://66.media.tumblr.com/868e5b2061c69445f2f634c51a2764f8/"
        "tumblr_p36zgwY6oS1virtjeo3_250.gif"
    )
