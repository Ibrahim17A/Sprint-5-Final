import random

class ComputerPlayer:
    def __init__(self, board_size):
        self.column = 0
        self.row = 0
        self.letter = ''
        self.board_size = board_size
    def pick_column(self):
        self.column = random.randint(0, self.board_size - 1)
    def pick_row(self):
        self.row = random.randint(0,self.board_size - 1)
    def pick_letter(self):
        random_letter = random.randint(1, 2)
        if random_letter == 1:
            self.letter = 'S'
        elif random_letter == 2:
            self.letter = 'O'

    def complete_computer_turn(self):
        self.pick_column()
        self.pick_row()
        self.pick_letter()

    





