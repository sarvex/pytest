import pytest


def test_foo():
    pass


@pytest.mark.parametrize("i", range(3))
def test_bar(i):
    pass
