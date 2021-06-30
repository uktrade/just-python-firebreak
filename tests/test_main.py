import unittest

from just_python import main


class TestMain(unittest.TestCase):
    def test_main(self):
        res = main.main()
        self.assertIs(res, True)
