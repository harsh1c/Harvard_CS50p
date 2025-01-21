import pytest
from seasons import words_convert
from seasons import minute_conversion
def test_two_years_ago():
    assert words_convert("2022-12-14") == "One million, fifty-two thousand, six hundred forty minutes"

