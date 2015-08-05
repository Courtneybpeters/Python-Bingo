import pygame, sys
from pygame.locals import *

class Game:
    called = []
    bg_color = pygame.Color(33, 17, 68)
    font_color = pygame.Color(125, 194, 187)
    buttons = {} # List of buttons Key = Name:Value = rect

    def __init__(self, player, surface):
        self.player = player
        self.screen = surface
        self.screen_rect = surface.get_rect()
        self.center = self.screen_rect.center

    def text(self, msg, font, color=font_color, x=0, y=0, button=False):
        text_surf = font.render(msg, True, color)
        text_rect = text_surf.get_rect()
        text_rect.center = self.center
        text_rect.x += x
        text_rect.y += y
        if button:
            self.buttons[msg] = text_rect

        self.draw(text_surf, text_rect)

    def draw(self, surf, rect):
        self.screen.blit(surf, rect)

    def clicked(self, click):
        for name, rect in self.buttons.iteritems(): # need values
            if rect.collidepoint(click):
                return name # return name of the rect

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
        ball = self.called[len(self.called) - 1]
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
