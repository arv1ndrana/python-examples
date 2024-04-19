#CLASS
class Number:
    def __init__(self, value):
        self.value = value

#DATACLASS

from dataclasses import dataclass

@dataclass
class Number:
    value:int

obj = Number(2)
print(obj.value)

class Human:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

@dataclass
class Human: # SUPPORTS DEFAULT
    name:str = "Adam"
    age: float= "30.5"
    sex: str = "Male"

Silvia = Human("Silvia")

print(Silvia.name)
print(Silvia.age)
print(Silvia.sex)

