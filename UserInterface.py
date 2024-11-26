# Game Logic Class
class UserInterface:
    def __init__(self, board_size):
        self.game_mode = ''

        self.board_size = board_size # Initializing board size

        self.board = [['' for _ in range(board_size)] for _ in range(board_size)] # 2D Board
        # The starting player will be blue
        self.current_player = 'blue'
        self.blue_player_win_count = 0 # starts at 0
        self.red_player_win_count = 0 # starts at 0
        self.tile_count = board_size * board_size
        self.turn_count = 1

    def set_game_mode(self, game_mode):
        self.game_mode = game_mode
        
    def make_move(self, row, col, letter,buttons):
        # Check if the selected cell is empty
        if self.is_cell_empty(row, col):
            # Place the letter in the cell
            self.board[row][col] = letter 
            buttons[row][col].config(text=letter)  # Update the button text
            # Update the button color based on the current player            
            buttons[row][col].config(fg=f"{self.current_player}")
        else:
            # Raise an error if the cell is already occupied
            raise ValueError("Cell is already occupied.")
        
    def is_cell_empty(self, row, col):
        if self.board[row][col] == '':
            return True

    def switch_turn(self):
        # Toggle the current turn between 'blue' and 'red'
        self.current_player = 'red' if self.current_player == 'blue' else 'blue'

    def check_game_end(self, row, col, current_letter, buttons):
        self.simple_game_ended = False
        win_count = 0

        # Vertical and horizontal
        if current_letter == 'S':
            letter_O = 'O'

            if row+2 < self.board_size and self.board[row+1][col] == letter_O :
                #check same direction for another S
                if self.board[row+2][col] == current_letter:
                    self.simple_game_ended = True  
                    win_count = win_count+1     
                    buttons[row][col].config(bg=f"{self.current_player}",fg="black") # Used to turn the letters on the board to black, because the dissapeard when the tiles switched colors when the SOS sequence was created
                    buttons[row+1][col].config(bg=f"{self.current_player}",fg="black") # Used to turn the letters on the board to black, because the dissapeard when the tiles switched colors when the SOS sequence was created 
                    buttons[row+2][col].config(bg=f"{self.current_player}",fg="black") # Used to turn the letters on the board to black, because the dissapeard when the tiles switched colors when the SOS sequence was created
            if row-2 >= 0 and self.board[row-1][col] == letter_O :
                #check same direction for another S
                if self.board[row-2][col] == current_letter:
                    self.simple_game_ended = True
                    win_count = win_count+1
                    buttons[row][col].config(bg=f"{self.current_player}",fg="black") # Used to turn the letters on the board to black, because the dissapeard when the tiles switched colors when the SOS sequence was created
                    buttons[row-1][col].config(bg=f"{self.current_player}",fg="black") # Used to turn the letters on the board to black, because the dissapeard when the tiles switched colors when the SOS sequence was created
                    buttons[row-2][col].config(bg=f"{self.current_player}",fg="black") # Used to turn the letters on the board to black, because the dissapeard when the tiles switched colors when the SOS sequence was created
            if col+2 < self.board_size and self.board[row][col+1] == letter_O :
                #check same direction for another S
                if self.board[row][col+2] == current_letter:
                    self.simple_game_ended = True
                    win_count = win_count+1
                    buttons[row][col].config(bg=f"{self.current_player}",fg="black") # Used to turn the letters on the board to black, because the dissapeard when the tiles switched colors when the SOS sequence was created
                    buttons[row][col+1].config(bg=f"{self.current_player}",fg="black") # Used to turn the letters on the board to black, because the dissapeard when the tiles switched colors when the SOS sequence was created
                    buttons[row][col+2].config(bg=f"{self.current_player}",fg="black") # Used to turn the letters on the board to black, because the dissapeard when the tiles switched colors when the SOS sequence was created
            if col-2 >= 0 and self.board[row][col-1] == letter_O :
                #check same direction for another S
                if self.board[row][col-2] == current_letter:
                    self.simple_game_ended = True
                    win_count = win_count+1
                    buttons[row][col].config(bg=f"{self.current_player}",fg="black") # Used to turn the letters on the board to black, because the dissapeard when the tiles switched colors when the SOS sequence was created
                    buttons[row][col-1].config(bg=f"{self.current_player}",fg="black") # Used to turn the letters on the board to black, because the dissapeard when the tiles switched colors when the SOS sequence was created
                    buttons[row][col-2].config(bg=f"{self.current_player}",fg="black") # Used to turn the letters on the board to black, because the dissapeard when the tiles switched colors when the SOS sequence was created
            if row-2 >= 0 and col-2 >= 0 and self.board[row-1][col-1] == letter_O :          
                #check same direction for another S
                if self.board[row-2][col-2] == current_letter:
                    self.simple_game_ended = True
                    win_count = win_count+1
                    buttons[row][col].config(bg=f"{self.current_player}",fg="black") # Used to turn the letters on the board to black, because the dissapeard when the tiles switched colors when the SOS sequence was created
                    buttons[row-1][col-1].config(bg=f"{self.current_player}",fg="black") # Used to turn the letters on the board to black, because the dissapeard when the tiles switched colors when the SOS sequence was created
                    buttons[row-2][col-2].config(bg=f"{self.current_player}",fg="black") # Used to turn the letters on the board to black, because the dissapeard when the tiles switched colors when the SOS sequence was created
            if row-2 >= 0 and col+2 < self.board_size and self.board[row-1][col+1] == letter_O :          
                #check same direction for another S
                if self.board[row-2][col+2] == current_letter:
                    self.simple_game_ended = True
                    win_count = win_count+1
                    buttons[row][col].config(bg=f"{self.current_player}",fg="black") # Used to turn the letters on the board to black, because the dissapeard when the tiles switched colors when the SOS sequence was created
                    buttons[row-1][col+1].config(bg=f"{self.current_player}",fg="black") # Used to turn the letters on the board to black, because the dissapeard when the tiles switched colors when the SOS sequence was created
                    buttons[row-2][col+2].config(bg=f"{self.current_player}",fg="black") # Used to turn the letters on the board to black, because the dissapeard when the tiles switched colors when the SOS sequence was created
            if row+2 < self.board_size and col+2 < self.board_size and self.board[row+1][col+1] == letter_O :          
                #check same direction for another S
                if self.board[row+2][col+2] == current_letter:
                    self.simple_game_ended = True
                    win_count = win_count+1
                    buttons[row][col].config(bg=f"{self.current_player}",fg="black") # Used to turn the letters on the board to black, because the dissapeard when the tiles switched colors when the SOS sequence was created
                    buttons[row+1][col+1].config(bg=f"{self.current_player}",fg="black") # Used to turn the letters on the board to black, because the dissapeard when the tiles switched colors when the SOS sequence was created
                    buttons[row+2][col+2].config(bg=f"{self.current_player}",fg="black") # Used to turn the letters on the board to black, because the dissapeard when the tiles switched colors when the SOS sequence was created
            if row+2 < self.board_size and col-2 >= 0 and self.board[row+1][col-1] == letter_O :          
                #check same direction for another S
                if self.board[row+2][col-2] == current_letter:
                    self.simple_game_ended = True
                    win_count = win_count+1
                    buttons[row][col].config(bg=f"{self.current_player}",fg="black") # Used to turn the letters on the board to black, because the dissapeard when the tiles switched colors when the SOS sequence was created
                    buttons[row+1][col-1].config(bg=f"{self.current_player}",fg="black") # Used to turn the letters on the board to black, because the dissapeard when the tiles switched colors when the SOS sequence was created
                    buttons[row+2][col-2].config(bg=f"{self.current_player}",fg="black") # Used to turn the letters on the board to black, because the dissapeard when the tiles switched colors when the SOS sequence was created
        # If the last played letter is 'O'
        elif current_letter == 'O':
            letter_S = 'S'

            if row+1 < self.board_size and self.board[row+1][col] == letter_S :
                #check opposite direction for another S
                if row-1 >= 0 and self.board[row-1][col] == letter_S:
                    self.simple_game_ended = True
                    win_count = win_count+1
                    buttons[row][col].config(bg=f"{self.current_player}",fg="black") # Used to turn the letters on the board to black, because the dissapeard when the tiles switched colors when the SOS sequence was created
                    buttons[row+1][col].config(bg=f"{self.current_player}",fg="black") # Used to turn the letters on the board to black, because the dissapeard when the tiles switched colors when the SOS sequence was created
                    buttons[row-1][col].config(bg=f"{self.current_player}",fg="black") # Used to turn the letters on the board to black, because the dissapeard when the tiles switched colors when the SOS sequence was created
            if col+1 < self.board_size and self.board[row][col+1] == letter_S :
                #check opposite direction for another S
                if col-1 >= 0 and self.board[row][col-1] == letter_S:
                    self.simple_game_ended = True
                    win_count = win_count+1
                    buttons[row][col].config(bg=f"{self.current_player}",fg="black") # Used to turn the letters on the board to black, because the dissapeard when the tiles switched colors when the SOS sequence was created
                    buttons[row][col+1].config(bg=f"{self.current_player}",fg="black") # Used to turn the letters on the board to black, because the dissapeard when the tiles switched colors when the SOS sequence was created
                    buttons[row][col-1].config(bg=f"{self.current_player}",fg="black") # Used to turn the letters on the board to black, because the dissapeard when the tiles switched colors when the SOS sequence was created
            if row+1 < self.board_size and col+1 < self.board_size and self.board[row+1][col+1] == letter_S :
                #check opposite direction for another S
                if row-1 >= 0 and col-1 >= 0 and self.board[row-1][col-1] == letter_S:
                    self.simple_game_ended = True
                    win_count = win_count+1
                    buttons[row][col].config(bg=f"{self.current_player}",fg="black") # Used to turn the letters on the board to black, because the dissapeard when the tiles switched colors when the SOS sequence was created
                    buttons[row+1][col+1].config(bg=f"{self.current_player}",fg="black") # Used to turn the letters on the board to black, because the dissapeard when the tiles switched colors when the SOS sequence was created
                    buttons[row-1][col-1].config(bg=f"{self.current_player}",fg="black") # Used to turn the letters on the board to black, because the dissapeard when the tiles switched colors when the SOS sequence was created
            if row+1 < self.board_size and col-1 >= 0 and self.board[row+1][col-1] == letter_S :
                #check opposite direction for another S
                if row-1 >= 0 and col+1 < self.board_size and self.board[row-1][col+1] == letter_S:
                    self.simple_game_ended = True
                    win_count = win_count+1
                    buttons[row][col].config(bg=f"{self.current_player}",fg="black") # Used to turn the letters on the board to black, because the dissapeard when the tiles switched colors when the SOS sequence was created
                    buttons[row+1][col-1].config(bg=f"{self.current_player}",fg="black") # Used to turn the letters on the board to black, because the dissapeard when the tiles switched colors when the SOS sequence was created
                    buttons[row-1][col+1].config(bg=f"{self.current_player}",fg="black") # Used to turn the letters on the board to black, because the dissapeard when the tiles switched colors when the SOS sequence was created
        if self.game_mode == "Simple Game":
            if self.simple_game_ended == True:
                return True
        elif self.game_mode == "General Game":
            if self.current_player == 'blue':
                self.blue_player_win_count = self.blue_player_win_count + win_count 
            else:
                self.red_player_win_count = self.red_player_win_count + win_count
            # Checking whether the General Game has ended when the board is full and it announces the winner or if it's a draw 
            if self.turn_count == self.tile_count:
                return True
        return False
    
    def record_game(self, file_path="record_sos_game.txt", buttons=None):
   
        try:
            with open(file_path, "w") as file:
                
                for i, row in enumerate(self.board):
                    row_data = []
                    for j, cell in enumerate(row):
                        fg_color = buttons[i][j].cget("fg") if buttons else "black"
                        bg_color = buttons[i][j].cget("bg") if buttons else "white"
                        row_data.append(f"{cell}:{fg_color}:{bg_color}")
                    file.write(",".join(row_data) + "\n")

                file.write(f"Current Player: {self.current_player}\n")
                file.write(f"Blue Wins: {self.blue_player_win_count}\n")
                file.write(f"Red Wins: {self.red_player_win_count}\n")
                file.write(f"Turn Count: {self.turn_count}\n")

            print("Game successfully recorded.")

        except Exception as e:
            print(f"An error occurred while recording the game: {e}")

            
    def replay_game(self, file_path="record_sos_game.txt", buttons=None):

        try:
            with open(file_path, "r") as file:
                lines = file.readlines()
            board_lines = lines[:-4]
            for i, line in enumerate(board_lines):
                row_data = line.strip().split(",")
                for j, cell_data in enumerate(row_data):
                    parts = cell_data.split(":")
                    cell = parts[0]
                    fg_color = parts[1] if len(parts) > 1 else "black"
                    bg_color = parts[2] if len(parts) > 2 else "white"

                    self.board[i][j] = cell
                    if buttons:
                        buttons[i][j].config(text=cell, fg=fg_color, bg=bg_color)

            self.current_player = lines[-4].split(": ")[1].strip()
            self.blue_player_win_count = int(lines[-3].split(": ")[1].strip())
            self.red_player_win_count = int(lines[-2].split(": ")[1].strip())
            self.turn_count = int(lines[-1].split(": ")[1].strip())

            print("Replay completed successfully.")

        except Exception as e:
            print(f"An error occurred while replaying the game: {e}")

