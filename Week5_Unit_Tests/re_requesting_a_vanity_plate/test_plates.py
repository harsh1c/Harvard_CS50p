from plates import is_valid

def test_two_letters():
    assert is_valid("11") == False

def test_max6_letters():
    assert is_valid("aaaaaaa") == False

def test_no_number_middle():
    assert is_valid("aa22a") == False

def test_no_zero_middle():
    assert is_valid("aa022") == False

def test_no_punctuation():
    assert is_valid("aa.22") == False