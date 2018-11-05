
import unittest
import app


class BasicFullTest(unittest.TestCase):
    def setUp(self):
        self.app = app.app.test_client()
        self.app.testing = True

    def test_trivial(self):
        response = self.app.post('/bot/janet', data=dict(
            token='sesame'
        ))
        assert b"Hi, there!" in response.data

    def test_badjanet(self):
        response = self.app.post('/bot/badjanet', data=dict(
            token='sesame'
        ))
        assert b'sup, _dinks_' in response.data

    def test_atl(self):
        response = self.app.post("/bot/janet", data=dict(
            token='sesame',
            text='atl'
        ))
        assert b"Russ" in response.data

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
