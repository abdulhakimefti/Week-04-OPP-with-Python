
class Animal:
    def __init__(self,name) -> None:
        self.name = name
    def make_sound(self):
        print("Animal making some sound")


class Cat(Animal):
    def __init__(self, name) -> None:
        super().__init__(name)
    def make_sound(self):
        print('meow')

class Dog(Animal):
    def __init__(self, name) -> None:
        super().__init__(name)
    def make_sound(self):
        print('bark bark')
don = Cat('don')
don.make_sound()
shephard  = Dog('German Shephard')
shephard.make_sound()
don2 = Cat('don2')

animals = [don,shephard,don2]

for animal in animals:
    animal.make_sound()