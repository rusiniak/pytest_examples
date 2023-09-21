import math

import pytest


@pytest.mark.parametrize("input ", [1, 4, 0])
@pytest.mark.parametrize("expected", [1, 4, 0])
def test_parametrized(input, expected):
    assert math.sqrt(input) - expected < 0.001


def test_parametrized_2(input_1, expected_1):
    assert math.sqrt(input_1) - expected_1 < 0.001