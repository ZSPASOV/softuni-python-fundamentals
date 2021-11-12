class Weapon:
    def __init__(self, bullets):
        self.bullets = bullets
    def shoot(self):
        if self.bullets > 0:
            self.bullets -= 1
            message = 'shooting...'
        else:
            message = 'no bullets left'
        return message
    def __repr__(self):
        return f'Remaining bullets: {self.bullets}'

weapon = Weapon(5)
weapon.shoot()
weapon.shoot()
weapon.shoot()
weapon.shoot()
weapon.shoot()
weapon.shoot()
print(weapon) # that is implicit calling of .__repr() method
# print(weapon) and print(weapon.__repr__()) is the same
# even if we do not assign .__repr__() method on the class object, it is automatically called on the background
print(weapon.__repr__()) # that is explicit calling of .__repr() method


