# Create a class Person that has, first name, last name and age

class Person:
    def __init__(self, first_name, last_name, age=0):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age


# When a parameter is optional, put a default value that it should have