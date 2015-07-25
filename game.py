import pygame, sys
from pygame.locals import *

class Game:
    selected = []
    bg_color = pygame.Color(33, 17, 68)

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
            choice = input("Your selection: ")

        return choice

    def ball_call(self):
        ball = self.selected[len(self.selected) - 1]
        print
        if ball < 16:
            print "-" * 8
            print "|   " + 'B' + str(ball) + "   |"
            print "-" * 8
        elif ball >= 16 and ball < 31:
            print "-" * 8
            print "|   " + 'I' + str(ball) + "   |"
            print "-" * 8
        elif ball >= 31 and ball < 46:
            print "-" * 8
            print "|   " + 'N' + str(ball) + "   |"
            print "-" * 8
        elif ball >= 46 and ball < 61:
            print "-" * 8
            print "|   " + 'G' + str(ball) + "   |"
            print "-" * 8
        elif ball >= 61 and ball < 75:
            print "-" * 8
            print "|   " + 'O' + str(ball) + "   |"
            print "-" * 8
