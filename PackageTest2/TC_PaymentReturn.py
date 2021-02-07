import unittest


class PaymentReturnTest(unittest.SkipTest):
    def test_paymentreturnbybank(self):
        print('this is payment return by the bank')
        self.assertTrue(True)


if __name__ == "__main__":
    unittest.main()