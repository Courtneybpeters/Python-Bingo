class Player:

    play = True
    wins = 0
    losses = 0


    def __init__(self, name=None):
        if name is not None:
            self.name = name

    def calculate_average(self):
        average = wins / losses
        return average
