from weapon import Weapon

class Robot:
    def __init__(self, name) -> None:
        self.name = name
        self.health = 100
        self.active_weapon= Weapon("Nerf Gun", 30)
    
    def attack(self,dinosaur):
        print()
        print (f"Robot {self.name} attacked Dinosaur {dinosaur.name}")
        dinosaur.health -= self.active_weapon.attack_power
        print(self.active_weapon.attack_power)
        if dinosaur.health < 0:
            dinosaur.health = 0    
        print(f"Dinosaur {dinosaur.name}'s health is now at {dinosaur.health}")
        print()
        
