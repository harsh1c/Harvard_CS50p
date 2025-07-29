
from bank import value

def test_hello():
    assert value("hello, bro") == 0

def test_h():
    assert value("hey, bro") == 20

def test_anything():
    assert value("sup, bro") == 100

def test_case_insensitivity():
    assert value("Hello, bro") == 0