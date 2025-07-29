import pytest
from fuel import convert,gauge

def test_convert():
    assert convert("1/2") == 50

def test_value_error():
    with pytest.raises(ValueError):
        convert("1/cat")

def test_zero_div():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")

def test_e():
    assert gauge(1) == "E"

def test_f():
    assert gauge(99) == "F"

def test_percent():
    assert gauge(10) == "10%"