# You can change the values of the attributes of an object after initialization


class Person:
    def __init__(self, first_name, last_name, age=0):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age


me = Person('Peter', 'Johnson', 25)
me.age += 1
print(me.age)