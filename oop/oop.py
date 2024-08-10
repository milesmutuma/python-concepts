class Monster:

    def __init__(self, health, energy):
        print("monster was created")
        self.health = health
        self.energy = energy

    def __len__(self):
        return self.health

    def __abs__(self):
        return self.energy

    def __str__(self):
        return (f"A monster with health of {self.health} "
                f"and energy of {self.energy}")

    def attack(self):
        print("monster has been attacked")
        print(self)


monster = Monster(100, 120)
print(monster)
# print(monster.health)
# print(monster.attack())
