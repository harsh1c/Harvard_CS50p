from twttr import shorten

def test_str():
    assert shorten("twitter") == "twttr"

def test_capital():
    assert shorten("TwItter") == "Twttr"

def test_number():
    assert shorten("twitter12") == "twttr12"

def test_punctuation():
    assert shorten("twitter.!") == "twttr.!"