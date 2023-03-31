from robot import Robot
from dinosaur import Dinosaur

class Battlefield:
    def __init__(self) -> None:
        self.robot = Robot('Ralphie')
        self.dinosaur = Dinosaur('Louise', 10)

    def run_game(self):
        print('Run Game')

    def display_welcome(self):
        print(" Welcome to Robot vs. Dinosaur")
        print()
        print(f" The robot is named {self.robot.name} and the dinosaur is named {self.dinosaur.name}")
        print()

    def battle_phase(self):
        print(" In Battle phase")

    def display_winner(self):
        print( "Winner")









