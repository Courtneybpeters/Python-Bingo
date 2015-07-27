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
    pygame.init()
    fpsClock = pygame.time.Clock()

    screen = pygame.display.set_mode((800, 480))
    pygame.display.set_caption('Pyngo')

    # TODO: Need player input on very beginning start_menu
    player = Player("Courtney")
    game = Game(player)

    state = 'new game'

    while True:
        if state == 'new game':
            game.start_menu(screen)





        screen.fill(game.bg_color)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.event.post(pygame.event.Event(QUIT))

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
