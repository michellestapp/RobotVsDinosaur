from robot import Robot
from dinosaur import Dinosaur

class Battlefield:
    def __init__(self) -> None:
        self.robot = Robot('Ralphie')
        self.dinosaur = Dinosaur('Louise', 10)

    def run_game(self):
        self.display_welcome()
        while self.dinosaur.health >= 0 or self.robot.health >= 0:
            self.battle_phase()

    def display_welcome(self):
        print(" Welcome to Robot vs. Dinosaur")
        print()
        print(f" The robot is named {self.robot.name} and the dinosaur is named {self.dinosaur.name}")
        print()

    def battle_phase(self):
        print(" In Battle phase")
        self.robot.attack(self.dinosaur)
        self.dinosaur.attack(self.robot)

    def display_winner(self):
        print( "Winner")









