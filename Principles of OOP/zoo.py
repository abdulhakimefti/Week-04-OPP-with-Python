from abc import ABC, abstractmethod
# abstract class


class Animal:
    @abstractmethod
    def eat(self):
        pass

    @property
    @abstractmethod
    def name(self):
        pass

    @abstractmethod
    def move(self):
        pass


class Monkey(Animal):
    def __init__(self):
        self.__name = 'monkey'

    def eat(self):
        pass

    def move(self):
        pass

    def sing(self):
        print('Monkeyis singing')

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value


layka = Monkey()
layka.name = 'MOOnkey'
print(layka.name)
