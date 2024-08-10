# def update_health(amount):
#     monster.health += amount


class Monster:
    def __init__(self, health, energy):
        self.health = health
        self.energy = energy

    def update_energy(self, amount):
        self.energy += amount


monster = Monster(health=100, energy=30)

print(monster.health)
