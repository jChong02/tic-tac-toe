class TicTacToeGame:

    
    def __init__(self):
        self.board = [""] * 9
        self.winner = ""
        self.moves = 0
        
    def getMark(self, pos):
        return self.board[pos]
    
    def getMoves(self):
        return self.moves
    
    def getWinner(self):
        return self.winner
    
    
    def placeX(self, pos):
        if self.board[pos] == "":
            self.board[pos] = "X"
            self.moves += 1
            return True
        return False
    
    def placeO(self, pos):
        if self.board[pos] == "":
            self.board[pos] = "O"
            self.moves += 1
            return True
        return False
    
    def checkWin(self):
        if self.checkRows() != "":
            self.winner = self.checkRows()
            return
        if self.checkCols() != "":
            self.winner = self.checkCols()
            return
        if self.checkDiagonals() != "":
            self.winner = self.checkDiagonals()
            return
        self.winner = ""
        return
            
    def checkRows(self):
        if self.board[0] == self.board[1] == self.board[2] != "":
            return self.board[0]
        if self.board[3] == self.board[4] == self.board[5] != "":
            return self.board[3]
        if self.board[6] == self.board[7] == self.board[8] != "":
            return self.board[6]        
        return ""
    
    def checkCols(self):
        if self.board[0] == self.board[3] == self.board[6] != "":
            print(self.board[0])
            return self.board[0]
        if self.board[1] == self.board[4] == self.board[7] != "":
            return self.board[1]
        if self.board[2] == self.board[5] == self.board[8] != "":
            return self.board[2]        
        return ""    
    
    def checkDiagonals(self):
        if self.board[0] == self.board[4] == self.board[8] != "":
            return self.board[0]
        if self.board[2] == self.board[4] == self.board[6] != "":
            return self.board[2]
        return ""    
    
            

