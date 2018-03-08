import pytest
from main import calcDistance


def TestDistance():
    a = [20, 2]
    b = [0.5, 5]

    d = calcDistance(a, b)
    assert d == pytest.approx(19.7294)
