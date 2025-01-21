from jar import Jar


def test_init():
    ...


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == '🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪'


def test_withdraw():
    jar = Jar()
    jar.deposit(12)
    jar.withdraw(1)
    assert str(jar) == '🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪'

def test_size():
    jar = Jar()
    assert jar.size == 0  # Initial size should be 0
    jar.deposit(5)
    assert jar.size == 5  # Size should be 5 after depositing 5 cookies
    jar.withdraw(2)
    assert jar.size == 3  # Size should be 3 after withdrawing 2 cookies