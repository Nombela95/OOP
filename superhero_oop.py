# Parent Class - Superhero
class Superhero:
    """A class representing a Superhero."""

    def __init__(self, name, power, strength_level):
        """Initialize superhero with name, power, and strength."""
        self.name = name  # Public attribute
        self._power = power  # Protected attribute
        self.__strength_level = strength_level  # Private attribute

    def introduce(self):
        """Introduce the superhero."""
        return f"I am {self.name}, and my superpower is {self._power}!"

    def get_strength_level(self):
        """Getter for private attribute strength_level."""
        return self.__strength_level

    def set_strength_level(self, new_level):
        """Setter for private strength_level (ensuring valid values)."""
        if new_level > 0:
            self.__strength_level = new_level
        else:
            print("Strength level must be positive!")

# Subclass 1 - Flying Superhero
class FlyingHero(Superhero):
    """A superhero who can fly."""
    
    def __init__(self, name, power, strength_level, flight_speed):
        """Initialize flying superhero with additional attribute."""
        super().__init__(name, power, strength_level)
        self.flight_speed = flight_speed  # New attribute for flying speed

    def introduce(self):
        """Override introduce method to include flying ability."""
        return f"I am {self.name}, I can {self._power} and fly at {self.flight_speed} km/h!"

# Subclass 2 - Speedster Superhero
class Speedster(Superhero):
    """A superhero with super speed."""
    
    def __init__(self, name, power, strength_level, speed):
        """Initialize speedster superhero with additional speed attribute."""
        super().__init__(name, power, strength_level)
        self.speed = speed  # New attribute for speed

    def introduce(self):
        """Override introduce method to include super speed ability."""
        return f"I am {self.name}, I can {self._power} and run at {self.speed} km/h!"

# Testing the classes
if __name__ == "__main__":
    hero1 = Superhero("Thor", "control thunder", 95)
    hero2 = FlyingHero("Superman", "super strength", 100, 500)
    hero3 = Speedster("Flash", "super speed", 80, 1200)

    print(hero1.introduce())
    print(f"Strength Level: {hero1.get_strength_level()}")

    print(hero2.introduce())
    print(hero3.introduce())

    # Testing encapsulation (attempting to access private attribute)
    hero1.set_strength_level(98)  # Updating strength level
    print(f"Updated Strength Level: {hero1.get_strength_level()}")
