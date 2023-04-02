import os
import time

from termcolor import colored
from controller import Controller

from player import Player


class ViewConsole:
    def __init__(self, controller: Controller):
        self.controller = controller

    def start(self):
        self.display_info()
        while True:
            self.move()

    def display_info(self):
        field = self.controller.get_field()
        os.system("CLS")
        self.draw_border()
        for field in field.field:
            self.draw(field)
        self.draw_border()

    def draw(self, field):
        for index, sign in enumerate(field):
            if sign == ['-']:
                self.__draw_field(field, index, sign)
            else:
                self.__draw_characters(field, index, sign)

    def __draw_field(self, field, index, sign):
        self.__check_end_list(field, index, sign)

    def __draw_characters(self, field, index, sign):
        for ch in self.controller.get_characters():
            if sign == ch.sign:
                sign = f"['{sign}']"
                self.__check_end_list(field, index, colored(sign, ch.colour))
                break

    def __check_end_list(self, field, index, sign):
        if len(field) - 1 == index:
            self.__draw_sign(sign, '\n')
        else:
            self.__draw_sign(sign)

    @staticmethod
    def draw_border():
        print(colored("-", "red") * 50)

    @staticmethod
    def __draw_sign(sign, ending=''):
        print(sign, end=ending)

    def win_check(self):
        lst = self.controller.get_characters()
        if len(lst) == 1:
            if isinstance(lst[0], Player):
                print("ВЫ ВЫЖИЛИ!")
            else:
                print("К сожалению, вы проиграли...")
            return 'ex'

    def move(self):
        try:
            move = self.win_check()
            if move is None:
                move = input(' Влево(a) Вниз(s) Вверх(w) Вправо(d)\n '
                             ' Атака(e) Выход(ex)\n')

            if move in 'weasdex':
                match move:
                    case 'a' | 's' | 'w' | 'd':
                        self.controller.move(move)
                    case 'e':
                        self.damage(self.controller.attack())
                    case 'ex':
                        exit()
            else:
                self.validation()
            self.controller.is_dead()
            self.display_info()
        except Exception as e:
            print(e)
            self.move()

    @staticmethod
    def validation():
        print("Ведено неверное значение")

    @staticmethod
    def damage(character):
        if character is not None:
            print(f'{character.name} получил урон: {character.hp}')
        time.sleep(1)
