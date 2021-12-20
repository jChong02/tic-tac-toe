import tkinter as tk
from TicTacToeGame import TicTacToeGame
from functools import partial

board = TicTacToeGame()
turn = "X"
gameEnd = False

window = tk.Tk()
window.grid_columnconfigure(0, weight=1)
window.title("Tic-Tac-Toe")
window.geometry("300x300")
window.maxsize(300,300)
window.minsize(300,300)

frm_board = tk.Frame(master=window)

frm_turn = tk.Frame(master=window)

def refreshBoard():
    for widget in frm_board.winfo_children():
        widget.destroy()
    pos = 0
    for i in range(3):
        for j in range(3):
            label = tk.Label(master=frm_board, height=5, width=10 ,text=board.getMark(pos), relief=tk.SOLID)
            if board.getMark(pos) == "X":
                label.config(fg= "Red")
            if board.getMark(pos) == "O":
                label.config(fg= "Blue")
            label.grid(row=i, column=j)
            placeMarker = partial(placeMarkerWithPos, pos)
            label.bind('<Button-1>', placeMarker)
            pos += 1
    if turn == "X":
        lbl_turn.config(text= "O's turn")
    else:
        lbl_turn.config(text= "X's turn")


def placeMarkerWithPos(pos, event):
    global turn, gameEnd
    lbl_error = tk.Label(master=frm_turn, text="You cannot place a marker there!", fg="Red")    
               
    if board.getMark(pos) != "" and not gameEnd:
        lbl_error.grid(row=1)
        lbl_error.after(500 , lambda: lbl_error.destroy())
    if turn == "X" and board.getMark(pos) == "" and board.getWinner() == "":
        board.placeX(pos)
        refreshBoard()
        turn = "O"
    if turn == "O" and board.getMark(pos) == "" and board.getWinner() == "":
        board.placeO(pos)
        refreshBoard()
        turn = "X"
    if board.getMoves() > 4:
        board.checkWin()
        if board.getWinner() != "":
            gameEnd = True
            lbl_turn.destroy()
            frm_winner = tk.Frame(master=window)
            lbl_winner = tk.Label(master=frm_winner, text="Winner is " + board.getWinner() + "!")
            if board.getWinner() == "X":
                lbl_winner.config(fg="Red")
            else:
                lbl_winner.config(fg="Blue")
            lbl_winner.grid()
            frm_winner.grid()
        if board.getMoves() == 9 and board.getWinner() == "":
            gameEnd = True
            lbl_turn.destroy()
            frm_winner = tk.Frame(master=window)
            lbl_winner = tk.Label(master=frm_winner, text="It's a draw!")
            lbl_winner.grid()
            frm_winner.grid()    
     
        

def createBoard():
    pos = 0
    for i in range(3):
        for j in range(3):
            label = tk.Label(master=frm_board, height=5, width=10 ,text=board.getMark(pos), relief=tk.SOLID)
            placeMarker = partial(placeMarkerWithPos, pos)
            label.bind('<Button-1>', placeMarker)
            label.grid(row=i, column=j)
               
            pos += 1
        


      
          

createBoard()

lbl_turn = tk.Label(master=frm_turn, text= turn+"'s turn")
lbl_turn.grid()

frm_board.grid(row=0,pady=(0,10))
frm_turn.grid()

window.mainloop()