# Реализовать класс - наследник от Mob. (моб - бос)
# НЕ переопределять получение урона.
# Создать два собственных уникальных метода.
# (Например, телепортацию и урон по окружающим клеткам)
from random import random

from character import Character


class Boss(Character):

    def __init__(self, clothes, hat):
        self._name = 'Boss'
        self._hp = 250
        self._attack = 20
        self._sign = '&'
        self._colour = 'red'
        self._step = 1
        self.clothes = clothes
        self.hat = hat

        super().__init__(self._name, self._hp, self._attack, self._sign, self._colour, self._step)


    def teleport(self, field, move, player):
        self.move_type(field, move)
        self.attack(player)

    def review(self):
        step = self._step
        y, x = self._place
        re = super().review()
        re['left_down'] = [y + step, x - step]
        re['right_down'] = [y + step, x + step]
        re['left_up'] = [y - step, x - step]
        re['right_up'] = [y - step, x + step]
        return re

    def attack(self):
        get_damages = []
        damage = random.randint(0, self._attack)
        for key in self.review_attr.keys():
            for character in self.characters:
                if key != 'cp' and self.review_attr[key] == character.place:
                    get_damages.append(character.get_damage(damage))
        return get_damages
