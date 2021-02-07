import unittest


class SignUpTest(unittest.TestCase):
    def test_SignUpByEmail(self):
        print('this SignUp by email')
        self.assertTrue(True)

    def test_SignUpByReverbnation(self):
        print('this SignUp by reverb')
        self.assertTrue(True)

    def test_SignUpByLinkedIn(self):
        print('this SignUp by linkedin')
        self.assertTrue(True)


if __name__ == "__main__":
    unittest.main()
