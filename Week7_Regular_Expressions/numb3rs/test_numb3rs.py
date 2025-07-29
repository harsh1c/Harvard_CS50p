from numb3rs import validate

def test_ip1():
   assert validate("1.1.1.1") == True

def test_ip3():
   assert validate("cat") == False

def test_ip4():
   assert validate("266.1.1.1") == False