import tkinter as tk
from tkinter import messagebox

class Board:

    # Initializing the board attributes
    def __init__(self, root):
        self.root = root
        # Creating 3x3 grid for the buttons
        self.buttons = [
            [None, None, None],
            [None, None, None],
            [None, None, None]
        ]

    # Creating a 3x3 board of buttons
    def create_board(self, click): 
        for i in range(3):
            for j in range(3):
                button = tk.Button(self.root, text = "", width = 5, height = 3, 
                            font =("Arial", 28), command = lambda i = i, j = j: click(i,j))
                button.grid(row = i, column = j)
                self.buttons[i][j] = button

    # Updating button at (row, col) with "X" or "O"
    def update_board(self, row, col, player):
        self.buttons[row][col].config(text = player)

class TicTacToe:

    # Initializing the game attributes
    def __init__(self, root):
        self.root = root
        self.current_player = "X"
        self.board = Board(root)
        self.board.create_board(self.clicking)

    # Switching player 1 to player 2 ("X" to "O")
    def switch_player(self):
        if self.current_player == "X":
            self.current_player = "O"
        else:
            self.current_player = "X"

    # Clicking a cell
    def clicking(self, row, col):
        if self.board.buttons[row][col].cget("text") == "":
            self.board.update_board(row, col, self.current_player)
            # Delaying it, so the players can see the final move
            self.root.after(100, self.check_game_state)

    # Checking the game state after a short delay to show the final move
    def check_game_state(self):
        if self.check_winner():
            messagebox.showinfo("Game Over", f"Player {self.current_player} wins!")
            self.reset_game()
        elif all(self.board.buttons[i][j].cget("text") != "" for i in range(3) for j in range(3)):
            messagebox.showinfo("Game Over", "It's a tie!")
            self.reset_game()
        else:
            self.switch_player()
    
    # Checking rows, columns and diagonals to see whether there is a winner or not
    def check_winner(self):
        for i in range(3):
            # Checking rows and columns
            if self.board.buttons[i][0].cget("text") == self.board.buttons[i][1].cget("text") == self.board.buttons[i][2].cget("text") != "":
                return True
            if self.board.buttons[0][i].cget("text") == self.board.buttons[1][i].cget("text") == self.board.buttons[2][i].cget("text") != "":
                return True
        # Checking diagonals    
        if self.board.buttons[0][0].cget("text") == self.board.buttons[1][1].cget("text") == self.board.buttons[2][2].cget("text") != "":
                return True
        if self.board.buttons[0][2].cget("text") == self.board.buttons[1][1].cget("text") == self.board.buttons[2][0].cget("text") != "":
                return True
        return False

    # Clears the board, starts a new game
    def reset_game(self):
        for i in range(3):
            for j in range(3):
                self.board.buttons[i][j].config(text = "")
        self.current_player = "X"

# Starting the game
root = tk.Tk()
root.title("Tic-Tac-Toe")
game = TicTacToe(root)
root.mainloop()