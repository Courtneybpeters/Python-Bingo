import random

class BingoBlower:
    # TODO: I have multiple bingo = 'bingo' assignments. Fix?
    balls = range(1, 76)
    random.shuffle(balls)

    def __init__(self):
        pass

    def get_ball(self):
        ball = self.balls.pop()
        return ball
