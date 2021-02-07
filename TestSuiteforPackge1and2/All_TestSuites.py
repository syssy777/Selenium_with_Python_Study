import unittest
from PackageTest1.TC_LoginTest import LoginTest
from PackageTest1.TC_SignUpTest import SignUpTest

from PackageTest2.TC_PaymentTest import PaymentTest
from PackageTest2.TC_PaymentReturn import PaymentReturnTest

# Get all test from the 2 package tests
tc_1 = unittest.TestLoader().loadTestsFromTestCase(LoginTest)
tc_2 = unittest.TestLoader().loadTestsFromTestCase(SignUpTest)
tc_3 = unittest.TestLoader().loadTestsFromTestCase(PaymentTest)
tc_4 = tc_Login = unittest.TestLoader().loadTestsFromTestCase(PaymentReturnTest)


'''# SANITY TEST SUITE are categorized as Sign up and Log in.
sanityTestSuite = unittest.TestSuite([tc_1,tc_2])
unittest.TextTestRunner().run(sanityTestSuite)


# FUNCTIONAL TEST SUITE are categorized as Sign up and Log in.
functionalTestSuite = unittest.TestSuite([tc_3,tc_4])
unittest.TextTestRunner().run(functionalTestSuite)'''

# MASTER TEST SUITE are categorized as Sign up and Log in.
masterTestSuite = unittest.TestSuite([tc_1,tc_2,tc_3,tc_4])
unittest.TextTestRunner(verbosity=2).run(masterTestSuite)



