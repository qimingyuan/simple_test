from add import add_qiming

def test_add():
    assert add_qiming(1, 1) == 2
    assert add_qiming(1, 2) == 3
    assert add_qiming(3, 4) == 7
    assert add_qiming(6, 5) == 11
