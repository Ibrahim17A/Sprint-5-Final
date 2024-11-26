from GameMode import GameMode
from tkinter import messagebox

# This class extends GameMode
class GeneralGame(GameMode):
    def __init__(self, board_size, isBluePlayerComputer, isRedPlayerComputer):
        super().__init__(board_size, isBluePlayerComputer, isRedPlayerComputer)
        self.UI.set_game_mode("General Game")
        self.blue_player_score_board = ''
        self.red_player_score_board = ''

    def make_move(self, row, col, current_letter, buttons):
        if self.UI.current_player == 'blue':
            if self.isBluePlayerComputer==True:
                current_letter = self.computer_player.letter
            else:
                current_letter = current_letter
        else:
            if self.isRedPlayerComputer ==True:
                current_letter = self.computer_player.letter
            else:
                current_letter = current_letter
        try:
            self.UI.make_move(row, col, current_letter, buttons)  # Attempt to make the move
            self.game_ended = self.UI.check_game_end(row, col, current_letter, buttons)  
            self.UI.record_game(file_path="record_sos_game.txt", buttons=buttons)

            self.update_current_player_score(self.blue_player_score_board, self.red_player_score_board)

            if (self.game_ended != True):
                # Switch to the other player's turn
                self.UI.switch_turn()
                self.UI.turn_count = self.UI.turn_count+1
                self.set_current_player_label(self.current_player_label)  # Update the current player label

                if (self.UI.current_player == 'blue' and self.isBluePlayerComputer ==True) or (self.UI.current_player == 'red' and self.isRedPlayerComputer ==True) :
                        self.get_computer_next_turn()
                        self.make_move(self.computer_player.row, self.computer_player.column, current_letter, buttons)
            elif self.game_ended == True: # Checking whether the General Game has ended when the board is full and it announces the winner or if it's a draw 
                if self.UI.blue_player_win_count == self.UI.red_player_win_count:
                    print("down here")
                    messagebox.showinfo("WHO WON?", "IT'S A DRAW!")
                elif self.UI.blue_player_win_count > self.UI.red_player_win_count:
                    messagebox.showinfo("WIN", "BLUE WON!!!!!!!")
                elif self.UI.red_player_win_count > self.UI.blue_player_win_count:
                    messagebox.showinfo("WIN", "RED WON!!!!!!!!")
        except ValueError as e:
            messagebox.showerror("Error", str(e))  # Show error message if the move is invalid

    def update_current_player_score(self, blue_player_score_board, red_player_score_board):
        self.blue_player_score_board = blue_player_score_board
        self.red_player_score_board = red_player_score_board
        blue_player_score_board.config(text=f"Score: {self.get_blue_player_win_count()}")
        red_player_score_board.config(text=f"Score: {self.get_red_player_win_count()}")