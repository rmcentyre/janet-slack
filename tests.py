
import unittest
from app import app
import time
from common.functions import slack_request_validation, compute_signature


class BasicFullTest(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
        # self.api = api

    def test_trivial(self):
        response = self.app.post('/bot/janet', data=dict())
        assert b"Hi, there!" in response.data

    def test_badjanet(self):
        response = self.app.post('/bot/badjanet', data=dict())
        assert b'sup, _dinks_' in response.data

    def test_atl(self):
        response = self.app.post('/bot/janet', data=dict(
            text='atl'
        ))
        assert b"Russ" in response.data

    def tearDown(self):
        pass


class ValidationTest(unittest.TestCase):
    signature = 'v0=bbad12cccf7b5a782948f38ed7a63d63f18ced606fa50ed257f61f8bfb684490'
    timestamp = '1550000000'
    body = 'blah blah blah'

    def test_valid(self):
        assert slack_request_validation(self.signature, self.timestamp, self.body, False)

    def test_timing(self):
        assert not slack_request_validation(self.signature, self.timestamp, self.body)

    def test_both(self):
        timestamp = f'{int(time.time())}'
        signature = compute_signature(timestamp, self.body)
        assert slack_request_validation(signature, timestamp, self.body)

    def test_signature(self):
        actual = compute_signature(self.timestamp, self.body)
        expected = self.signature
        assert expected == actual


if __name__ == '__main__':
    unittest.main()