class Dinosaur:
    def __init__(self, name, attack_power):
        self.name = name
        self.attack_power = attack_power
        self.health = 100

    def attack(self, robot):
        print()
        print(f" Dino {self.name} attacked Robot {robot.name}")
        robot.health -= self.attack_power
        if robot.health < 0:
            robot.health = 0    
        print(f" Robot {robot.name}'s health score is now {robot.health}")
        print()
  