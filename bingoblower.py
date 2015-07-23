import random

class BingoBlower:
    # TODO: I have multiple bingo = 'bingo' assignments. Fix?
    bingo = 'bingo'
    selected = {}

    def __init__(self):
        pass

    def get_ball(self):
        column = self.bingo[random.randrange(len(self.bingo))]
        print column.upper()
