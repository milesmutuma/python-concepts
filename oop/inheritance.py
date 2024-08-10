class Monster:
    def __init__(self, health, energy):
        self.health = health
        self.energy = energy

    def attack(self, amount):
        print("The monster has attacked!")
        print(f"{amount} damage was dealt")
        self.energy -= 10

    def move(self, speed):
        print("The monster has moved")
        print(f"It has a speed of {speed}")


class Shark(Monster):
    def __init__(self, health, energy, speed):
        super().__init__(health, energy)
        self.speed = speed

    def bite(self):
        print("The shark has bitten")

    def move(self, speed):
        print("The shark has moved")
        print(f"It has a speed of {speed}")


shark = Shark(speed=120, health=1500, energy=100)
print(shark.health)
