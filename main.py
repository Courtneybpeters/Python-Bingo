from player import Player
from game import Game
from bingocard import BingoCard
from bingoblower import BingoBlower
import pygame, sys
from pygame.locals import *


"""
BINGO:
  - Bingo Card class (card with the random numbers)
  - Bingo Blower class (machine that generates numbers)
  - Player class (track wins/losses and dabs)

"""
def main():
    # TODO: Should I put the main loop in game as well?
    pygame.init()
    fpsClock = pygame.time.Clock()

    title = "Python Bingo"
    width = 800
    height = 480

    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption(title)

    center = screen.get_rect().center

    big_font = pygame.font.Font("assets/FredokaOne-Regular.ttf", 80)
    sm_font = pygame.font.SysFont("helvetica", 24)

    new_msg = "New game"


    # TODO: Need player input on very beginning start_menu
    player = Player("Courtney")
    game = Game(player, screen)

    state = 'start'

    while True:
        if state == 'start':
            screen.fill(game.bg_color)
            title_rect = game.text(title, big_font, y=-40)
            new_rect = game.text(new_msg, sm_font, y=50, True)

        elif state == 'in game':
            screen.fill(game.bg_color)
            



        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.event.post(pygame.event.Event(QUIT))
            elif event.type == MOUSEBUTTONDOWN:
                click = event.pos
                selection = game.clicked(click)
                if selection == title:
                    print "Title clicked"
                elif selection == new_msg:
                    state = 'in game'


        pygame.display.update()
        fpsClock.tick(30)

    print
    print "Welcome to Courtney's Pyngo - Bingo in Python."
    choice = game.start_menu()

    if choice == 1:
        card = BingoCard()
        card.draw_bingocard()
    elif choice == 2:
        # I'm letting player handle everything
        # Would I want average so I can send it to other classes possibly?
        calculate_average()

    blower = BingoBlower()

    for i in range(5):
        # TODO: WAITING/TIMING INPUT FUNCTION
        game.selected.append(blower.get_ball())
        game.ball_call()



if __name__ == "__main__":
    main()
