from ComputerPlayer import ComputerPlayer
from UserInterface import UserInterface

class GameMode():
    def __init__(self, board_size, isBluePlayerComputer, isRedPlayerComputer):
        self.board_size = board_size
        self.current_player_label = ''
        self.UI = UserInterface(board_size)
        
        self.isBluePlayerComputer = isBluePlayerComputer
        self.isRedPlayerComputer = isRedPlayerComputer        

        if isBluePlayerComputer or isRedPlayerComputer:
            self.computer_player = ComputerPlayer(board_size)        

    def get_current_player(self):
        return self.UI.current_player

    def get_blue_player_win_count(self):
        return self.UI.blue_player_win_count
    
    def get_red_player_win_count(self):
        return self.UI.red_player_win_count

    def get_computer_next_turn(self):
        self.computer_player.complete_computer_turn()
        if self.UI.is_cell_empty(self.computer_player.row, self.computer_player.column):
            return True
        else:
            self.get_computer_next_turn()

    def set_current_player_label(self, current_player_label):
        self.current_player_label = current_player_label
        # Determine the current player's name and color for display
        current_player_name = "Blue" if self.get_current_player() == 'blue' else "Red"
        if current_player_name == 'Blue':
            current_player_label.config(text=f"Current Player: {current_player_name.upper()}", fg="blue")
        else:
            current_player_label.config(text=f"Current Player: {current_player_name.upper()}", fg="red")            
    