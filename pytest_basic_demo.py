import pytest

@pytest.fixture(scope="function")
def initial_setup():
    print("doing initial setup")

def test_function1(initial_setup):
    print("executing function1 test")