import pytest

# run this by typing 'cd followed by the package name', press enter and now type 'pytest -v -s
# followed by the file name and press enter.

@pytest.yield_fixture()
def setUp():
    print('Open browser to log in')
    yield
    print('Close browser after log in')


def test_SignUpByReverbnation():
    print('this login by reverb')


def test_SignUpByLinkedIn():
    print('this login by linkedin')



