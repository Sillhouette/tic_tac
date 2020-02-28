import unittest

from unittest.mock import call, Mock
from src.cli import Cli
from src.three_by_three_board import ThreeByThreeBoard

class CliTest(unittest.TestCase):
    def test_log_message(self):
        writer = Mock()
        cli = Cli(writer=writer)
        test_string = "Hello World"

        actual = cli.log(test_string)

        writer.assert_called_once_with(test_string)
    
    def test_prompt_user(self):
        reader = Mock()
        expected = "1"
        reader.return_value = expected
        cli = Cli(reader=reader)
        
        actual = cli.prompt_user()

        self.assertEqual(expected, actual)

    def test_prompt_user_2(self):
        reader = Mock()
        expected = "9"
        args = "Some prompt"
        reader.return_value = expected
        cli = Cli(reader=reader)

        actual = cli.prompt_user(args)
        
        reader.assert_called_once_with(args)
        self.assertEqual(expected, actual)

    def test_print_board_3x3(self):
        board = ThreeByThreeBoard()
        writer = Mock()
        cli = Cli(writer=writer)
        board.spaces = ["X", " ", " ", "O", " ", "X", " ", " ", "O"]
       
        expected = """
⊱ –––––– {⋆⌘⋆} –––––– ⊰

       X |   |   
      ---+---+---
       O |   | X 
      ---+---+---
         |   | O 

⊱ –––––– {⋆⌘⋆} –––––– ⊰
"""
        actual = cli.print_board(board)
        
        writer.assert_called_once_with(expected)

    def test_display_empty_3x3_board(self):
        board = ThreeByThreeBoard()
        writer = Mock()
        cli = Cli(writer=writer)

        expected =  """
⊱ –––––– {⋆⌘⋆} –––––– ⊰

         |   |   
      ---+---+---
         |   |   
      ---+---+---
         |   |   

⊱ –––––– {⋆⌘⋆} –––––– ⊰
"""
        actual = cli.display_3x3_board(board)

        writer.assert_called_once_with(expected)

    def test_display_3x3_board_in_progress(self):
        board = ThreeByThreeBoard()
        writer = Mock()
        cli = Cli(writer=writer)
        board.spaces = ["X", " ", " ", "O", " ", "X", " ", " ", "O"]
       
        expected = """
⊱ –––––– {⋆⌘⋆} –––––– ⊰

       X |   |   
      ---+---+---
       O |   | X 
      ---+---+---
         |   | O 

⊱ –––––– {⋆⌘⋆} –––––– ⊰
"""
        actual = cli.display_3x3_board(board)
        
        writer.assert_called_once_with(expected)

    def test_handle_exit(self):
        writer = Mock()
        cli = Cli(writer=writer)
        expected = Cli.MESSAGES[Cli.EXIT] 

        actual = cli.handle_exit()

        writer.assert_called_with(expected)

    def test_handle_game_end(self):
        writer = Mock()
        cli = Cli(writer=writer)
        expected = Cli.MESSAGES[Cli.FINISHED] 

        actual = cli.handle_game_end()

        writer.assert_called_with(expected)

    def test_welcome(self):
        writer = Mock()
        cli = Cli(writer=writer)
        expected = Cli.MESSAGES[Cli.WELCOME] 

        actual = cli.welcome()

        writer.assert_called_with(expected)

    def test_invalid_move(self):
        writer = Mock()
        cli = Cli(writer=writer)
        expected = Cli.MESSAGES[Cli.ERROR] 

        actual = cli.invalid_move()

        writer.assert_called_with(expected)

 
    def get_player_tokens(self):
        cli = Cli()
        expected = ["X", "O"]
        
        actual = cli.get_player_tokens()

        self.assertEqual(expected, actual)

    def get_board_type_3x3(self):
        cli = Cli()
        expected = "3x3"

        actual = cli.get_board_type()

        self.assertEqual(expected, actual)

    def request_move(self):
        player = Mock()
        player.token = "X"
        writer = Mock()
        cli = Cli(writer=writer)
        expected = "It's X's turn! Please select a square using 1-9:\n"

        actual = cli.request_move(player)

        self.assertEqual(expected, actual)

