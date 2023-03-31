class Dinosaur:
    def __init__(self, name, attack_power):
        self.name = name
        self.attack_power = 20
        self.health = 100

    def attack(self, robot):
        print(" Dino attacks Robot")