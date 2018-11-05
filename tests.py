
import unittest
import app


class BasicFullTest(unittest.TestCase):
    def setUp(self):
        self.app = app.app.test_client()
        self.app.testing = True

    def test_trivial(self):
        response = self.app.get('/')
        assert b"Warning: Not for human consumption!" in response.data

    def test_hello_world(self):
        response = self.app.post("/bot/hello", data=dict(
            token='sesame'
        ))
        assert b"Hello, world!" in response.data

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
