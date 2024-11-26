import unittest
from unittest.mock import MagicMock
from GameLogic import GameLogic

class TestCheckGameEnd(unittest.TestCase):
    # CHATGPT GENERATED
    # def test_check_game_end_simple_win(self):
    #     """Test that the game ends correctly when an SOS sequence is created in Simple Game mode."""
    #     gameLogic = GameLogic()
        
    #     # Set up the board for a winning condition in the Simple Game
    #     gameLogic.game.UI.board = [['', '', ''], 
    #                 ['O', '', ''], 
    #                 ['S', '', '']]
        
    #     # Mock the button objects
    #     buttons = [[MagicMock() for _ in range(3)] for _ in range(3)]
        
    #     # Set the current player and letter to create the winning sequence
    #     gameLogic.game.UI.current_player = 'blue'
    #     gameLogic.game.make_move(0, 0, 'S', buttons)

    #     # Assert that the game ended with a win
    #     self.assertTrue(gameLogic.game.UI.simple_game_ended, "The game should end when an SOS sequence is created.")
    #     buttons[0][0].config.assert_any_call(bg="blue", fg="black")  # Winning sequence coloring
    # # CHATGPT GENERATED
    # def test_check_game_end_general_mode_scores(self):
    #     """Test that the score is updated correctly when an SOS sequence is created in General Game mode."""
    #     gameLogic = GameLogic()
    #     gameLogic.Game_mode_var.set("General Game")
    #     gameLogic.new_game()
        
    #     # Set up the board for a scoring condition in the General Game
    #     gameLogic.game.UI.board = [['', '', ''], 
    #                 ['O', '', ''], 
    #                 ['S', '', '']]
        
    #     # Mock the button objects
    #     buttons = [[MagicMock() for _ in range(3)] for _ in range(3)]
        
    #     # Set the current player and make the move that completes an SOS sequence
    #     gameLogic.game.UI.current_player = 'blue'
    #     gameLogic.game.make_move(0, 0, 'S', buttons)
        
    #     # Assert that the blue player's score increased
    #     self.assertEqual(gameLogic.game.get_blue_player_win_count(), 1, "The blue player's score should increment by 1 after completing an SOS.")

    # # # personally created
    # def test_check_game_end_general_mode_scores_fail(self):
    #     """Test that the score is updated correctly when an SOS sequence is created in General Game mode."""
    #     gameLogic = GameLogic()
    #     gameLogic.Game_mode_var.set("General Game")
    #     gameLogic.new_game()

    #     # Mock the button objects
    #     buttons = [[MagicMock() for _ in range(3)] for _ in range(3)]
    #     # Set the current player and make the move that completes an SOS sequence
    #     gameLogic.game.UI.current_player = 'blue'
    #     gameLogic.game.make_move(0, 0, 'S', buttons)
    #     # Assert that the blue player's score increased
    #     self.assertNotEqual(gameLogic.game.get_blue_player_win_count(), 2, "If blue scores one point, his score should not be two.")

    # # # personally created
    # def test_simple_game_draw(self):
    #     gameLogic = GameLogic()
    #     # Mock the button objects
    #     buttons = [[MagicMock() for _ in range(3)] for _ in range(3)]
    #     # Set the current player and letter to create the winning sequence
    #     gameLogic.game.UI.turn_count = 9
    #     gameLogic.game.make_move(0, 0, 'S', buttons)
    #     # Assert that the game ended with a win
    #     self.assertTrue(gameLogic.game.UI.turn_count == gameLogic.game.UI.tile_count and gameLogic.game.game_ended != True, "This game should end in a draw")

    # # # personally created
    # def test_general_game_mode(self):
    #     gameLogic = GameLogic()
    #     gameLogic.Game_mode_var.set("General Game")
    #     gameLogic.new_game()
    #     # Mock the button objects
    #     buttons = [[MagicMock() for _ in range(3)] for _ in range(3)]
    #     # Set the current player and letter to create the winning sequence
    #     gameLogic.game.UI.blue_player_win_count = 5
    #     gameLogic.game.UI.red_player_win_count = 0
    #     gameLogic.game.UI.turn_count = gameLogic.game.UI.tile_count
    #     gameLogic.game.make_move(0, 0, 'S', buttons)
    #     # Assert that the game ended with a win
    #     self.assertTrue(gameLogic.game.UI.blue_player_win_count > gameLogic.game.UI.red_player_win_count, "Blue should win this game")
    
    # # # personally created
    # def test_draw_general_game_mode(self):
    #     gameLogic = GameLogic()
    #     gameLogic.Game_mode_var.set("General Game")
    #     gameLogic.new_game()
    #     # Mock the button objects
    #     buttons = [[MagicMock() for _ in range(3)] for _ in range(3)]
    #     gameLogic.game.UI.turn_count = gameLogic.game.UI.tile_count
    #     gameLogic.game.make_move(0, 0, 'S', buttons)
    #     # Assert that the game ended with a win
    #     self.assertTrue(gameLogic.game.UI.blue_player_win_count == gameLogic.game.UI.red_player_win_count, "This game should end in a draw")

    def test_computer_random_num_generator(self):
        gameLogic = GameLogic()
        gameLogic.blue_player_computer.set(True)
        gameLogic.new_game()

        cp = gameLogic.game.computer_player
        cp.complete_computer_turn()
        self.assertTrue(cp.letter != '', "Error: letter should not be empty")
        self.assertTrue(cp.row >= 0 and cp.row < cp.board_size, "Error: Row must be between 0 and board_size - 1")
        self.assertTrue(cp.column >= 0 and cp.column < cp.board_size, "Error: column must be between 0 and board_size - 1")
        
    def test_pick_unoccupied_cell(self):
        gameLogic = GameLogic()
        gameLogic.blue_player_computer.set(True)
        gameLogic.new_game()
        cp = gameLogic.game.computer_player

        # Set up the board for a winning condition in the Simple Game
        gameLogic.game.UI.board = [['S', '', ''], 
                    ['', '', ''], 
                    ['', '', '']]

        cp.row = 0
        cp.column = 0
        gameLogic.game.get_computer_next_turn()
        self.assertTrue(cp.row != 0 or cp.column != 0, "Error: get_computer_next_turn did not pick an empty cell")

# Running the tests
unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromTestCase(TestCheckGameEnd))

