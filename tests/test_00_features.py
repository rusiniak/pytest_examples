import pytest


def test_1(cache):
    print("test_1")
    assert True


def test_2(cache):
    print(cache.get("my_secret_key", None))
    assert False


def test_3():
    with pytest.raises(IOError):
        raise IOError

class CustomIOError(IOError):
    ...

def test_4():
    with pytest.raises(IOError):
        raise CustomIOError


def test_5():
    assert True
