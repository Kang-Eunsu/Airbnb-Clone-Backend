"""
class Human:
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print(f"Hello My Name is {self.name}")
        

class Player(Human):
    def __init__(self, name, xp):
        super().__init__(name)
        self.xp = xp

class Fan(Human):
    def __init__(self, name, fav_team):
        super().__init__(name)
        self.fav_team = fav_team
        

eunsu = Player("eunsu", 1000)
eunsu.say_hello()

sally = Fan("sally", "eunsu")
sally.say_hello()
"""


from typing import Any


class Dog:
    def __init__(self, name, xp):
        self.name = name
        self.xp = xp

    def __str__(self):
        return f"Dog : {self.name}"

    def __getattribute__(self, name):
        print(f"they want to get {name}")
        return "^^"


jia = Dog("jia", 1000)
print(jia.xp)
