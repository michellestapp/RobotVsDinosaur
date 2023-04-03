from weapon import Weapon

class Robot:
    def __init__(self, name) -> None:
        self.name = name
        self.health = 100
        self.active_weapon= Weapon('',0)
    
    def attack(self,dinosaur):
        print()
        print (f"Robot {self.name} attacked Dinosaur {dinosaur.name}")
        dinosaur.health -= self.active_weapon.attack_power
        print(self.active_weapon.attack_power)
        if dinosaur.health < 0:
            dinosaur.health = 0    
        print(f"Dinosaur {dinosaur.name}'s health is now at {dinosaur.health}")
        print()
        
    def choose_weapon(self,Weapon):
         print(f" Choose a weapon for robot {self.name}:")
         print()
         print(" Press '1' for a Nerf Gun with an attack power of 10")
         print(" Press '2' for a Light Saber with an attack power of 35")
         weapon_choice = input(" Press '3' for a Candlestick with an attack power of 15: ")
         if weapon_choice == '1':
            self.active_weapon.name = "Nerf Gun"
            self.active_weapon.attack_power = 10
         elif weapon_choice == '2':
            self.active_weapon.name = "Light Saber"
            self.active_weapon.attack_power = 35
         else:
            self.active_weapon.name = "Candlestick"
            self.active_weapon.attack_power = 15
     
         self.weapon = Weapon(self.active_weapon.name, self.active_weapon.attack_power)

         print(f" You have chosen a {self.weapon.name} as your robot's weapon")
         print()
