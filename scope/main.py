a = 10


def test_func():
    a = 20
    print(a)


test_func()


def test_func_2():
    global a
    a += 2
    print(a)


test_func_2()
