import random

class BingoCard:
    bingo = 'bingo'

    def __init__(self):
        self.card = [[0]* 5] * 5
        for col in range(len(self.card)):
            for row in range(len(self.card[col])):

                # This loop is really setting these groups through each row instead of column
                #ColBRow1 -> (1-15), ColBRow2 -> (16-31), etc
                for i in range(5):
                    start = (i * 15) + 1
                    end = (i + 1) * 15
                    num = random.randrange(start, (end + 1))
                    print "Num", num
                    self.card[col][row] = num
        # print "card", self.card

    def draw_bingocard(self):
        for char in self.bingo:
            print char,
        print
        print "-" * 10

        for col in self.card:
            for row in col:
                if col[row] == 4:
                    print "|" + row + "|"
                    print "_"
                else:
                    print "|" + row + "|"
