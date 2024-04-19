class Person:
    def __init__(self,name,age,country):
        self.name = name
        self.age = age
        self.country = country

    def speak(self):
        print(f"Hello! My name is {self.name}. I live in {self.country}. I am {self.age} years old.")

class Student(Person):
    def __init__(self, major):
        super().__init__(name,age, country)
        self.major = major

