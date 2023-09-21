import pytest


def pytest_generate_tests(metafunc: pytest.Metafunc):
    if "input_1" in metafunc.fixturenames:
        argnames = ["input_1", "expected_1"]
        argvalues = [(0, 0), (1, 1)]
        metafunc.parametrize(argnames, argvalues)