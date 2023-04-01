class Dinosaur:
    def __init__(self, name, attack_power):
        self.name = name
        self.attack_power = attack_power
        self.health = 200

    def attack(self, robot):
        print(f" Dino {self.name} attacked Robot {robot.name}")
        robot.health -= self.attack_power
        print(f" Robot {robot.name}'s health score is nnow {robot.health}")
        print(robot)
        