import pytest
import random, time


CHOICES = [1, 2, 3, 4]


def pytest_generate_tests(metafunc: pytest.Metafunc):
    if "input_1" in metafunc.fixturenames:
        argnames = ["input_1", "expected_1"]
        argvalues = [(0, 0), (1, 1)]
        metafunc.parametrize(argnames, argvalues)

@pytest.fixture(autouse=True, scope="session")
def return_random():
    print("initializing seed to 1")
    time_start = time.time()
    random.seed(1)
    yield random.choice(CHOICES)
    #teardown
    time_end = time.time()
    print(f"fixture was alive for {time_end - time_start} s")
