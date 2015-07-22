class Game:

    def __init__(self, player):
        self.player = player

    def menu(self):
        choice = 0

        while type(choice) is not int or (choice < 1 or choice > 4):
            print "Please enter a valid choice"
            print "1 - New Game"
            print "2 - Statistics"
            print "3 - Exit"
            print "-" * 80
            choice = input()

        return choice
