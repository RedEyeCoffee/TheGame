from random import randint
from character import Character


class Mob(Character):

    def __init__(self, clothes, hat):
        self._name = 'Mob'
        self._hp = 100
        self._attack = 10
        self._sign = '#'
        self._colour = 'red'
        self._step = 1
        self.clothes = clothes
        self.hat = hat

        super().__init__(
            self._name,
            self._hp,
            self._attack,
            self._sign,
            self._colour,
            self._step)

    @staticmethod
    def shout():
        print("Arrrrrgh!")

    @staticmethod
    def prize():
        items = ["money", "health", "map", "key", "glue", "weapon", "speed"]
        item = items[randint(0, 6)]
        print(item)
