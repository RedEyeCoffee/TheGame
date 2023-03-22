import os
import time

from character import Character
from controller import Controller
from termcolor import colored


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
                    print(ch.colour())
                    if val == ch.sign:
                        ch.colour = 'green'
                        if len(i) - 1 == j:
                            self.print_colour_ch(colored([val], str(ch.colour())), '\n')
                            break
                        else:
                            self.print_colour_ch(colored([val], str(ch.colour())))
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

    def move(self):
        try:
            move = int(input(f'1. Движение\n2. Атака\n3. Выход\n'))
            if int(move) == 1:
                move_side = int(input('1. Влево\n2. Вниз\n3. Вверх\n4. Вправо\n'))
                if 0 < move_side < 5:
                    self.controller.move(move_side)
                else:
                    self.validation()
            elif move == 2:
                self.damage(self.controller.attack())
            elif move == 3:
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
