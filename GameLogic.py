import tkinter as tk
from tkinter import messagebox

from GeneralGame import GeneralGame
from SimpleGame import SimpleGame

# GUI Class for the SOS Game
class GameLogic:
    def __init__(self):
        # Initializing the main window
        self.master = tk.Tk()
        self.master.title("SOS Game")
        # Setting the default size and game mode ( 3 & Simple game )
        self.board_size = 3
        # Holding the buttons for the game board
        self.board_buttons = []
        self.game_mode = "Simple Game"
        # THe defult letter when the game starts will be S for both ( Blue and Red)
        self.Player_letter_blue = 'S'
        self.Player_letter_red = 'S'
        
        # GUI widgets
        self.create_widgets()
        # new game
        self.new_game()

    def run(self):
        self.master.mainloop()

    def create_widgets(self): # creating the title of the game on the top left side of the board
        self.Game_title_label = tk.Label(self.master, text="SOS Game", font=("Arial", 18))
        self.Game_title_label.grid(row=0, column=0, pady=10, padx=10)

        self.Game_mode_var = tk.StringVar(value="Simple Game") # Creating a variable to hold the selected game mode

        # Radio buttons to select which game mode the  players want to choose ( simple or general)
        tk.Radiobutton(self.master, text="Simple Game", variable=self.Game_mode_var, value="Simple Game").grid(row=0, column=2)# Radio buttons to select which game mode the  players want to choose / Simple
        tk.Radiobutton(self.master, text="General Game", variable=self.Game_mode_var, value="General Game").grid(row=0, column=3)# Radio buttons to select which game mode the  players want to choose / General

        # Blue player will be playing on the left side of the board (this is the display of the "blue player")
        self.blue_player_label = tk.Label(self.master, text="Blue Player:", fg='blue')
        self.blue_player_label.grid(row=1, column=0, columnspan=2)

        # Variable to hold the currently selected letter
        self.blue_letter = tk.StringVar(value='S')
        self.blue_player_computer = tk.BooleanVar()
        
        tk.Radiobutton(self.master, text="S", variable=self.blue_letter, value='S').grid(row=2, column=0) # Blue player S
        tk.Radiobutton(self.master, text="O", variable=self.blue_letter, value='O').grid(row=3, column=0) # Blue player O
        tk.Checkbutton(self.master, text="Blue Computer", variable=self.blue_player_computer, onvalue=True, offvalue=False).grid(row=4, column=0) # Blue player O

        self.red_player_label = tk.Label(self.master, text="Red Player:", fg='red') # Red player label
        self.red_player_label.grid(row=1, column=7, columnspan=2, padx=10) # placement for red player label
        self.red_player_computer = tk.BooleanVar(value=False)
        self.red_letter = tk.StringVar(value='S') # Variable to hold the current value

        tk.Radiobutton(self.master, text="S", variable=self.red_letter, value='S').grid(row=2, column=7) # Red player S
        tk.Radiobutton(self.master, text="O", variable=self.red_letter, value='O').grid(row=3, column=7)  # Red player O
        tk.Checkbutton(self.master, text="Red Computer", variable=self.red_player_computer, onvalue=True, offvalue=False).grid(row=4, column=7)
        
        self.board_size_label = tk.Label(self.master, text="Board Size:") # Board size selection label
        self.board_size_label.grid(row=0, column=4, padx=10) # Board size selection label placement

        self.board_size_entry = tk.Entry(self.master, width=5, font="bold") # Box to enter the board size
        self.board_size_entry.grid(row=0, column=5, padx=10) #placement on the board
        self.board_size_entry.insert(0, str(self.board_size))  # Set the default size in the entry / 3
        
        self.board_frame = tk.Frame(self.master) # this is a frame to hold the board buttons
        self.board_frame.grid(row=1, column=1, columnspan=6, rowspan=6, pady=10) # placement

        self.blue_player_score_board = tk.Label(self.master, text="Score:", fg='blue') # Blue player score Label 
        self.blue_player_score_board.grid(row=5, column=0) # where it is placed

        self.red_player_score_board = tk.Label(self.master, text="Score:", fg='red') # Score label for red
        self.red_player_score_board.grid(row=5, column=7) # Score label placement

        self.current_player_label = tk.Label(self.master, text="Current Player: Blue", font=("Arial", 16, 'bold'), fg='blue') # Label to display the current players's name
        self.current_player_label.grid(row=7, column=0, columnspan=8, pady=10) #placement: under the board

        self.new_game_button = tk.Button(self.master, text="New Game", command=self.new_game, width=20, height=3) # Button to start a new game
        self.new_game_button.grid(row=8, column=5, pady=10, padx=10)

        self.record_game_button = tk.Button(self.master, text="Record Game", command=lambda: self.game.UI.record_game(file_path="record_sos_game.txt", buttons=self.board_buttons), width=20, height=3)
        self.record_game_button.grid(row=8, column=4, pady=10, padx=10)

        self.replay_game_button = tk.Button(self.master,text="Replay Game",command=lambda: self.game.UI.replay_game(file_path="record_sos_game.txt", buttons=self.board_buttons), width=20, height=3)
        self.replay_game_button.grid(row=8, column=6, pady=10, padx=10)


    def create_board(self): # Reseting the board and buttons
        for row in self.board_buttons:
            for btn in row:
                btn.grid_forget() 
        self.board_buttons = [] 
       
        for i in range(self.board_size): # Dynamic buttons based on board size
            row_buttons = []
            for j in range(self.board_size):
                btn = tk.Button(self.board_frame, text="", width=6, height=2, font=("Arial", 12, "bold"),
                                command=lambda i=i, j=j: self.on_cell_click(i, j), padx=0, pady=0)
                btn.grid(row=i, column=j)  # Place the button in the grid
                row_buttons.append(btn)  # Add the button to the row list
            self.board_buttons.append(row_buttons)  # Add the row to the board buttons list

    def on_cell_click(self, row, col):
        try:
            if self.game.get_current_player() == 'blue':
                current_letter = self.blue_letter.get()
            else:
                current_letter = self.red_letter.get()

            self.game.make_move(row, col, current_letter, self.board_buttons)  # Attempt to make the move

        except ValueError as e:
            messagebox.showerror("Error", str(e))  # Show error message if the move is invalid

    def new_game(self): # Making sure that the board size input is valid > 3
        
        try:
            board_size_input = self.board_size_entry.get()
            if board_size_input == "":
                self.board_size = 3  # Default size
            else:
                self.board_size = int(board_size_input)
            if self.board_size < 3:
                raise ValueError("Board size must be 3 or greater.")
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid integer for the board size (3 or greater).")
            return           
        
        # Get the selected game mode
        if self.Game_mode_var.get()  == "Simple Game":
            self.game = SimpleGame(self.board_size, self.blue_player_computer.get(), self.red_player_computer.get())
        else:
            self.game = GeneralGame(self.board_size, self.blue_player_computer.get(), self.red_player_computer.get())
            self.game.update_current_player_score(self.blue_player_score_board, self.red_player_score_board) # updates the score to 0

        self.create_board()  # Create a new game board

        # Reseting the game state based on the new board size and game mode
        self.game.set_current_player_label(self.current_player_label)  # Update the current player label

        if self.blue_player_computer.get() == True:
            self.game.get_computer_next_turn()
            self.game.make_move(self.game.computer_player.row, self.game.computer_player.column, self.game.computer_player.letter, self.board_buttons)
