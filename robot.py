from weapon import Weapon

class Robot:
    def __init__(self, name) -> None:
        self.name = name
        self.health = 100
        self.active_weapon= Weapon("Nerf gun",35)
    
    def attack(self,dinosaur):
        print (f"{self.name} attacked {dinosaur.name}")
        dinosaur.health -= self.active_weapon.attack_power
        print(f"Dinosaur {dinosaur.name}'s health is now at {dinosaur.health}")
        

