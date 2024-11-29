from um import count

def test_word():
     assert count("mum ") == 0
def test_space():
     assert count(" um um ") == 2
def test_counting():
     assert count("um um um") == 3
def test_case1():
     assert count("uM") == 1
def test_cae2():
     assert count("UM") == 1

