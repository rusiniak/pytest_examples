
CHOICES = [1, 2, 3, 4]





def test_random(return_random):
    assert return_random in CHOICES


def test_other_random(return_random):
    assert return_random in CHOICES

def test_not_requesting_fixture():
    assert True
