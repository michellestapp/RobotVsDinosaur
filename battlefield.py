from robot import Robot
from dinosaur import Dinosaur
from weapon import Weapon

class Battlefield:
    def __init__(self) -> None:
        self.robot = Robot('')
        self.dinosaur = Dinosaur('', 25)
        self.weapon = Weapon('',0)

    def run_game(self):
        self.display_welcome()
        self.battle_phase()
        self.display_winner()

    def display_welcome(self):
       
        print(" Welcome to Robot vs. Dinosaur")
        print()
        self.dinosaur.name = input(f" What is your dinosaur's name?")
        print()
        self.robot.name = input(f" What is your robot's name?")
        print(f" The robot is named {self.robot.name} and the dinosaur is named {self.dinosaur.name}")
        print()
        self.robot.choose_weapon(Weapon)


    def battle_phase(self):
        print(" In Battle phase")
        dinosaur_turn = True
        robot_turn = False
        while self.dinosaur.health > 0 and self.robot.health > 0:

            ready = input(" Press enter to start the next round! ")
            if ready == '':
                if dinosaur_turn == True:
                    
                    self.dinosaur.attack(self.robot)
                    dinosaur_turn = False
                    robot_turn = True
                else:
                    self.robot.attack(self.dinosaur)
                    dinosaur_turn = True
                    robot_turn = False
            

    def display_winner(self):
        if self.dinosaur.health != 0:
            print(f" Dinosuar {self.dinosaur.name} won the game!")
        else:
            print(f" Robot {self.robot.name} won the game!")










