def add(a, b):
    return a + b


class Test:
    def __init__(self, add_func):
        self.add_func = add_func


test = Test(add_func=add)
print(test.add_func(1, 2))


class Monster:
    def __init__(self, func):
        self.func = func


class Attacks:
    def bite(self):
        print("Bite")

    def slash(self):
        print("Bite")

    def strike(self):
        print("Strike")

    def kick(self):
        print("Strike")


attacks = Attacks()
monster = Monster(func=attacks.bite)
monster.func()
