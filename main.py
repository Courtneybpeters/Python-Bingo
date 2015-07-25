import player as p
import game as g
import bingocard as bc
import bingoblower as bb
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
    screen = pygame.display.set_mode((800, 480))
    pygame.display.set_caption('Pyngo')

    # TODO: Need player input on very beginning menu
    player = p.Player("Courtney")
    game = g.Game(player)

    while True:
        screen.fill(game.bg_color)

    print
    print "Welcome to Courtney's Pyngo - Bingo in Python."
    choice = game.menu()

    if choice == 1:
        card = bc.BingoCard()
        card.draw_bingocard()
    elif choice == 2:
        # I'm letting player handle everything
        # Would I want average so I can send it to other classes possibly?
        p.calculate_average()

    blower = bb.BingoBlower()

    for i in range(5):
        # TODO: WAITING/TIMING INPUT FUNCTION
        game.selected.append(blower.get_ball())
        game.ball_call()

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.event.post(pygame.event.Event(QUIT))

    pygame.display.update()

if __name__ == "__main__":
    main()
