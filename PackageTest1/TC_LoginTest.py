import unittest


class LoginTest(unittest.TestCase):
    def test_loginByEmail(self):
        print('this login by email')
        self.assertTrue(True)

    def test_loginByReverbnation(self):
        print('this login by reverb')
        self.assertTrue(True)

    def test_loginByLinkedIn(self):
        print('this login by linkedin')
        self.assertTrue(True)


if __name__ == "__main__":
    unittest.main()
