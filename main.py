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

    print
    print "Welcome to Courtney's Pyngo - Bingo in Python."
    choice = game.menu()

    if choice == 1:
        card = bc.BingoCard()
        card.draw_bingocard()
    elif choice == 2:
        # I'm letting player handle everything
        # Would I want average so I can send it to other classes possibly?
        p.calculate_average

    # Get ball and then have timed input
    blower = bb.BingoBlower()
    blower.get_ball()


if __name__ == "__main__":
    main()
