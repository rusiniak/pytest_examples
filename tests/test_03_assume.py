import pytest


@pytest.mark.skip()
def test_multiple_conditions():
    with pytest.assume:
        assert False, "broken test"
    result: int = 20
    with pytest.assume:
        assert result == 10 + 10
    result += 20
    with pytest.assume:
        assert result == 100 + 100

def test_multiple_conditions_2():
    # gather some test results
    # assume all(test_resuls
    assert False, "broken test"
    assert result == 10 + 10
    assert result == 100 + 100
