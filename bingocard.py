import random

class BingoCard:
    bingo = 'bingo'

    def __init__(self):
        self.card = [[0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0]]
        # Bingo columns (B, I, N, G, O)
        for col in range(len(self.card)):
            # Range grouping
            start = (col * 15) + 1
            end = (col + 1) * 15
            # Rows in Bingo Columns (5 below each letter)
            for row in range(len(self.card[col])):
                num = random.randrange(start, (end + 1))
                while num in self.card[col]:
                    num = random.randrange(start, (end + 1))
                self.card[col][row] = num

    def draw_bingocard(self):
        print
        print

        for char in self.bingo:
            print "   "+ char.upper() + "   ",
        print
        print "-" * 40

        for row in range(len(self.card[0])):
            for col in self.card:
                # Single digit column in B spacing
                if col[row] < 10:
                    print "| ", col[row], " |",
                # Last column to allow new line
                elif self.card.index(col) == len(self.card) - 1:
                    print "|", col[row], " |"
                    print "-" * 40
                else:
                    print "|", col[row], " |",
