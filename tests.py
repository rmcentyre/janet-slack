
import unittest


class BasicFullTest(unittest.TestCase):
    def setUp(self):
        pass

    def single_test(self):
        self.assertTrue(True)

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
