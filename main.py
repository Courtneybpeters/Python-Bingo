import player as p
import game as g
import bingocard as bc
import bingoblower as bb

"""
BINGO:
  - Bingo Card class (card with the random numbers)
  - Bingo Blower class (machine that generates numbers)
  - Player class (track wins/losses and dabs)

"""
def main():
    player = p.Player("Courtney")
    game = g.Game(player)

    print "Welcome to Courtney's Pyngo - Bingo in Python."
    choice = game.menu()

    if choice == 1:
        card = bc.BingoCard()
        card.draw_bingocard()
    elif choice == 2:
        print "To do"

if __name__ == "__main__":
    main()