from robot import Robot
from dinosaur import Dinosaur
from weapon import Weapon

class Battlefield:
    def __init__(self) -> None:
        self.robot = Robot('')
        self.dinosaur = Dinosaur('', 25)

    def run_game(self):
        self.display_welcome()
        self.battle_phase()
        self.display_winner()

    def display_welcome(self):
        weapon_choice = ''
        print(" Welcome to Robot vs. Dinosaur")
        print()
        self.dinosaur.name = input(f" What is your dinosaur's name?")
        print()
        self.robot.name = input(f" What is your robot's name?")
        print(f" The robot is named {self.robot.name} and the dinosaur is named {self.dinosaur.name}")
        print()
        # self.weapon = Weapon('',0)
        # print(f" Choose a weapon for robot {self.robot.name}:")
        # print()
        # print(" Press '1' for a Nerf Gun with an attack power of 10")
        # print(" Press '2' for a Light Saber with an attack power of 35")
        # weapon_choice = input(" Press '3' for a Candlestick with an attack power of 15: ")
        # if weapon_choice == 1:
        #     self.weapon.name = "Nerf Gun"
        #     self.weapon.attack_power = 10
        # elif weapon_choice == 2:
        #     self.weapon.name = "Light Saber"
        #     self.weapon.attack_power = 25
        # else:
        #     self.weapon.name = "Candlestick"
        #     self.weapon.attack_power = 15
        # self.weapon = Weapon(self.weapon.name, self.weapon.attack_power)

        # print(f" You have chosen a {self.weapon.name} as your robot's weapon")
        # print()
        

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










