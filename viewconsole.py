import os
import time

from character import Character
from controller import Controller
from termcolor import colored

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
        self.print_border()
        for i in field.field:
            for j, val in enumerate(i):
                for ch in self.controller.get_characters():
                    if val == ch.sign:
                        if len(i) - 1 == j:
                            self.print_colour_ch(colored([val], ch.colour), '\n')
                            break
                        else:
                            self.print_colour_ch(colored([val], ch.colour))
                            break
                if val == '-':
                    if len(i) - 1 == j:
                        self.print_colour_ch([val], '\n')
                    else:
                        self.print_colour_ch([val])
        self.print_border()

    @staticmethod
    def print_border():
        print(colored("-", "red") * 50)

    @staticmethod
    def print_colour_ch(sign, ending=''):
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
                move = input(f' Влево(a) Вниз(s) Вверх(w) Вправо(d)\n Атака(e) Выход(ex)\n')

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
