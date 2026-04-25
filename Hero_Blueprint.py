"""
-----------------------------------------------------------------------
ASSIGNMENT 14A: THE HERO BLUEPRINT
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. Define a class named 'Hero'.
[ ] 3. Use __init__ to give the hero a name and a power.
[ ] 4. Add a method 'intro' that prints "I am [name] and I use [power]!".
[ ] 5. Instantiate two hero objects and call their 'intro' method.
-----------------------------------------------------------------------
"""

class Hero:
    def __init__(self, name, power, team, rating):
        # Private attributes
        self.__name = name
        self.__power = power
        self.__team = team
        self.__rating = rating

    # Getters (Accessors)
    def get_name(self):
        return self.__name

    def get_power(self):
        return self.__power

    def get_team(self):
        return self.__team

    def get_rating(self):
        return self.__rating


    # Setters (Mutators)
    def set_name(self, name):
        self.__name = name

    def set_power(self, power):
        self.__power = power

    def set_team(self, team):
        self.__team = team

    def set_rating(self, rating):
        self.__rating = rating


    # Methods
    def intro(self):
        print(f"I am {self.get_name()}, I work with {self.get_team()}, and I use {self.get_power()}!")

    def show_rating(self):
        print(f"{self.get_name()}'s hero rating is {self.get_rating()}/10.")


# Creating hero objects
hero1 = Hero("Homelander", "laser eyes", "The Seven", 10)
hero2 = Hero("The Deep", "talking to fish", "The Seven", 4)
hero3 = Hero("Starlight", "light blasts", "The Seven", 7)
hero4 = Hero("Black Noir", "stealth combat", "The Seven", 9)
hero5 = Hero("Billy Butcher", "supe-destruction rage", "The Boys", 8)

heroes = [hero1, hero2, hero3, hero4, hero5]

for hero in heroes:
    hero.intro()
    hero.show_rating()
    print("-----")