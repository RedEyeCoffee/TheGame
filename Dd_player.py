import player
import random
import character

class Dd_Player(player.Player):

    def __init__(self):

        super().__init__(self)

    def review(self):
        step = 5
        cp = {}
        x, y = self._place
        cp['cp'] = self._place
        cp['left'] = [x, y - step]
        cp['down'] = [x + step, y]
        cp['up'] = [x - step, y]
        cp['right'] = [x, y + step]
        return cp