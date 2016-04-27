from random import randint

class connectFour:   
    def __init__ (self, rows = 7, col = 8, fourInRow = 4):
        #Creates the board
        self.col = col
        self.win = fourInRow
        self.rows = rows
        self.board = [['.'] * rows for _ in range(col)]
    
    def insert(self, column, color):
        #Inserts the player's color when they choose a column
        c = self.board[column]
        if c[0] != '.':
            raise Exception('NO MORE!')
        i = -1
        while c[i] != '.':
            i -= 1
        c[i] = color
        self.checkWinner

    def checkWinner(self):
        #Checking for any winners on the board
        print('Checking if ' + player + ' is a winner...')
        w = self.Winner()
        if w:
            self.printBoard()
            raise Exception(w + ' Winner!')
        if (checkWinner('R')):
            print('RED WINS!')
        elif (checkWinner('Y')):
            print('YELLOW WINS!')

    def printBoard(self):
        #Prints the board
        print(' '.join(map(str, range(self.col))))
        for y in range(self.rows):
            print(' '.join(str(self.board[x][y]) for x in range(self.col)))


             
if __name__ == '__main__':
    four = connectFour()
    turn = 'R'
    while True:
        four.printBoard()
        row = input('{}\'s turn: '.format('Red' if turn == 'R' else 'Yellow'))
        four.insert(int(row), turn)
        turn = 'Y' if turn == 'R' else 'R'
        

      
    



    

