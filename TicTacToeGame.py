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
        for i in range(3):
            if self.board[i*3] == self.board[(i*3)+1] == self.board[(i*3)+2] != "":
                return self.board[i*3]
        return ""
    
    def checkCols(self):
        for i in range(3):
            if self.board[i] == self.board[i+3] == self.board[i+6] != "":
                return self.board[i]
        return ""
    
    def checkDiagonals(self):
        if self.board[0] == self.board[4] == self.board[8] != "":
            return self.board[0]
        if self.board[2] == self.board[4] == self.board[6] != "":
            return self.board[2]
        return ""    
    
            

