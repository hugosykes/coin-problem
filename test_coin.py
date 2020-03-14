from coin import make_change


def test_zero():
    assert make_change(total=0, coins=[]) == 0


def test_no_coins():
    assert make_change(total=125, coins=[]) == 0


def test_4__1_2():
    assert make_change(total=4, coins=[1, 2]) == 3


def test_5__1_2():
    assert make_change(total=5, coins=[1, 2]) == 3


def test_6__1_2():
    assert make_change(total=6, coins=[1, 2]) == 4


def test_6__2():
    assert make_change(total=6, coins=[2]) == 1


def test_10__1_2_5():
    assert make_change(total=10, coins=[1, 2, 5]) == 10


def test_10__3():
    assert make_change(total=10, coins=[3]) == 0


def test_10__1_3():
    assert make_change(total=10, coins=[1, 3]) == 4
