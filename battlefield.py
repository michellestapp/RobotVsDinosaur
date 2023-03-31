from robot import Robot
from dinosaur import Dinosaur

class Battlefield:
    def __init__(self) -> None:
        self.robot = Robot()
        self.dinosaur = Dinosaur()

    def run_game(self):
        print('Run Game')

    def display_welcome(self):
        print(" Welcome for Robot vs. Dinosaur")

    def battle_phase(self):
        print(" In Battle phase")

    def display_winner(self):
        print( "Winner")

        







