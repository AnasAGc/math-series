from math_series.series import *
from math_series import __version__

def test_version():
    assert __version__ == '0.1.0'

def test_zero():
    expected=0
    actual=fibonacci(0)
    assert expected==actual

def test_one():
    expected=1
    actual=fibonacci(1)
    assert expected==actual

def test_seven():
    expected=8
    actual=fibonacci(7)
    assert expected==actual


def test_zero_for_lucas():
    expected=2
    actual=lucas(0)
    assert expected==actual
def test_one_for_lucas():
    expected=1
    actual=lucas(1)
    assert expected==actual
def test_seven_for_lucas():
    expected=18
    actual=lucas(7)
    assert expected==actual

def test_zero_for_other():
    expected=0
    actual=sum_series(0)
    assert expected==actual
def test_one_for_other():
    expected=3
    actual=sum_series(1,4,3)
    assert expected==actual

def test_seven_for_other():
    expected=137
    actual=sum_series(7,9,5)
    assert expected==actual
  