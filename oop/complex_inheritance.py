class Monster:
    def __init__(self, health, energy, **kwargs):
        self.health = health
        self.energy = energy
        super().__init__(**kwargs)

    def attack(self, amount):
        print("The monster has attacked!")
        print(f"{amount} damage was dealt")
        self.energy -= 10

    def move(self, speed):
        print("The monster has moved")
        print(f"It has a speed of {speed}")


class Fish:
    def __init__(self, speed, has_scales, **kwargs):
        self.speed = speed
        self.has_scales = has_scales
        super().__init__(**kwargs)

    def swim(self):
        print(f"The fish has a speed of {self.speed}")


class Shark(Monster, Fish):
    def __init__(self, bite_strength, health, energy, speed, has_scales):
        self.bite_strength = bite_strength
        super().__init__(health, energy, speed=speed, has_scales=has_scales)

    def get_bite_strength(self):
        return self.bite_strength
# MRO - Method resolution order
