class Superhero:
    def __init__(self, name, power_level=100, health=100):
        self.name = name
        self.power_level = power_level
        self.health = health
    
    def attack(self, opponent):
        damage = self.power_level // 10
        opponent.health -= damage
        print(f"{self.name} attacks {opponent.name} for {damage} damage!")
    
    def display_status(self):
        print(f"{self.name}: Power={self.power_level}, Health={self.health}")

class FlyingSuperhero(Superhero):
    def __init__(self, name, power_level=100, health=100, flight_speed=50):
        super().__init__(name, power_level, health)
        self._flight_speed = flight_speed  # Encapsulated private attribute
    
    def attack(self, opponent):  # Polymorphic override: stronger attack with flight bonus
        damage = (self.power_level // 10) + (self._flight_speed // 5)
        opponent.health -= damage
        print(f"{self.name} dive-bombs from the sky, attacking {opponent.name} for {damage} damage!")
    
    def fly(self):
        print(f"{self.name} soars at {self._flight_speed} mph!")  # Fixed: Added self.

# Example usage: Creating objects with unique values
hero1 = Superhero("Captain Strength", power_level=150, health=120)
hero2 = FlyingSuperhero("Skyhawk", power_level=120, health=110, flight_speed=80)

print("Initial Status:")
hero1.display_status()
hero2.display_status()

print("\nAttacking each other:")
hero1.attack(hero2)
hero2.attack(hero1)

print("\nUpdated Status:")
hero1.display_status()
hero2.display_status()

print("\nFlying demonstration:")
hero2.fly()