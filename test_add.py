from add import add_qiming, Add

def test_add():
    assert add_qiming(1, 1) == 2
    assert add_qiming(1, 2) == 3
    assert add_qiming(3, 4) == 7
    assert add_qiming(6, 5) == 11

def test_add_class():
    add = Add()
    assert add.apply(1, 1) == 2
    assert add.apply(3, 4) == 7
    assert add.apply(5, 6) == 11

