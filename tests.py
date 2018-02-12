
import unittest
import janet


class BasicFullTest(unittest.TestCase):
    def setUp(self):
        self.app = janet.app
        self.app.testing = True

    def test_trivial(self):
        with self.app.test_client() as c:
            response = c.get('/')
            assert b"Warning: Not for human consumption!" in response.data

    def test_hello_world(self):
        with self.app.test_client() as c:
            response = c.post("/bot/hello", data=dict(
                token='sesame'
            ))
            assert b"Hello, world!" in response.data

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
