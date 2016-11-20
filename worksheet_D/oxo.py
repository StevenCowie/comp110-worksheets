class OxoBoard:
    def __init__(self):
        #Initialises board array
        self.game_Board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]


    def get_square(self, x, y):
        #Returns 0, 1 or 2 depending on the contents of the specified square.
        return  self.game_Board[x][y]


    def set_square(self, x, y, mark):
        #Checks content of square and fills empty spots with marks and returns True, is space is taken returns False
        if self.game_Board[x][y] == 0:
            self.game_Board[x][y] = mark
            return True
        else:
            return False


    def is_board_full(self):
        #Checks every square to see if there are any empty squares left, returns True if none are empty
        for x in xrange(3):
            for y in xrange(3):
                if self.game_Board[x][y] == 0:
                    return False
        return True
        #if it reaches this point no empty squares on board

    def get_winner(self):
        # Checks whole board to see if there are 3 in row (vertical, horizontal and diagonal)
        for i in xrange(3):
            if self.game_Board[i][0] == self.game_Board[i][1] and self.game_Board[i][2]!= 0:
                return self.game_Board[i][0]
            elif self.game_Board[0][i] == self.game_Board[1][i] and self.game_Board[2][i] != 0:
                return self.game_Board[0][i]
            if self.game_Board[0][0] == self.game_Board[1][1] and self.game_Board[2][2] != 0:
                return self.game_Board[0][0]
            if self.game_Board[0][2] == self.game_Board[1][1] and self.game_Board[2][0] != 0:
                return self.game_Board[0][2]
        return 0


    def show(self):
        """ Display the current board state in the terminal. """
        for y in xrange(3):
            if y > 0:
                print "--+---+--"
            for x in xrange(3):
                if x > 0:
                    print '|',

                # Print a space for empty (0), an O for player 1, or an X for player 2
                print " OX"[self.get_square(x, y)],
            print


def input_square():
    """ Prompt the player to enter a square. """
    while True:
        input = raw_input("Enter x,y where x=0,1,2, y=0,1,2: ")
        if input.count(',') != 1:
            print "Input must contain exactly one comma!"
            continue

        x, y = input.split(',')
        try:
            x = int(x)
            y = int(y)
        except ValueError:
            print "Input must be two numbers separated by a comma!"
            continue

        if x < 0 or x > 2 or y < 0 or y > 2:
            print "Input is out of bounds!"
            continue

        return x, y


# The main game. You should not need to edit this.
if __name__ == '__main__':
    board = OxoBoard()
    current_player = 1
    while True:
        board.show()
        print "Choose a square, Player", current_player
        x, y = input_square()

        if board.set_square(x, y, current_player):
            # Move was played successfully, so check for a winner
            winner = board.get_winner()
            if winner != 0:
                print "Player", winner, "wins!"
                break   # End the game
            elif board.is_board_full():
                print "It's a draw!"
                break   # End the game
            else:
                # Switch players
                if current_player == 1:
                    current_player = 2
                else:
                    current_player = 1
        else:
            # Move was not played successfully
            print "That square is already filled!"
