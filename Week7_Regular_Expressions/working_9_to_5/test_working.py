import pytest
from working import convert

def test_normal():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"

def test_no_to():
    with pytest.raises(ValueError):
        convert("9 AM-5 PM")


def test_out_of_range():
    with pytest.raises(ValueError):
        convert("9:60 AM to 5 PM")