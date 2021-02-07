import pytest

'''

# run this code by going to the terminal and type  pytest -v -s test_BasicPytest.py   and press enter.
def testMethod1():
    print( 'here is test 1')

def testMethod2():
    print( 'here is test 2')
'''

'''
# PYTEST FIXTURES ==================================================================================
@pytest.fixture()
def setUp():
    print('the set up runs once before a method')


def testMethod1(setUp):  # always pass the setUp method as parameter before the fixture function can work.
    print('here is test 1')


def testMethod2(setUp):
    print('here is test 2')

'''


@pytest.yield_fixture()  # always runs before and after each method below.
def setUp():
    print(' Runs once before a method')
    yield
    print(' Runs once after a method')


def testMethod3(setUp):  # always pass the setUp method as parameter before the fixture function can work.
    print('This is test 1')



def testMethod4(setUp):
    print('This is test 2')




