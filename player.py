class Player:

    __play = True
    __wins = 0
    __losses = 0


    def __init__(self, name=None):
        if name is not None:
            self.name = name

    def calculate_average(self):
        average = wins / losses
        print
        print "Winning Percentage: " + str(average) + "%"
