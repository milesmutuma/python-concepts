class Monster:
    """A monster that has attributes"""

    def __init__(self, health, energy, **kwargs):
        self.health = health
        self.energy = energy
        self._id = 5
        super().__init__(**kwargs)

    def attack(self, amount):
        print("The monster has attacked!")
        print(f"{amount} damage was dealt")
        self.energy -= 10

    def move(self, speed):
        print("The monster has moved")
        print(f"It has a speed of {speed}")


monster = Monster(10, 20)

print(hasattr(monster, 'health'))

setattr(monster, 'weapon', 100)

new_attrs = (['weapon', 'axe'], ['armor', 'Shield'], ['potion', 'mana'])

print(new_attrs)
print(type(new_attrs))

for attr, value in new_attrs:
    setattr(monster, attr, value)

print(vars(monster))

# Doc
