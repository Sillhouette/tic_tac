import unittest

from unittest.mock import call, Mock
from src.cli import Cli
from src.board import Board

class CliTest(unittest.TestCase):
    def test_log_message(self):
        mock = Mock()
        cli = Cli(mock)
        test_string = "Hello World"

        cli.log(test_string)

        mock.assert_called_once_with(test_string)
    
    def test_log_messages(self):
        mock = Mock()
        cli = Cli(mock)
        test_strings = ["Hello", "World"]
        calls = [call("Hello"), call("World")]

        cli.log(test_strings)

        mock.assert_has_calls(calls)

    def test_prompt_user(self):
        mock = Mock()
        expected = "1"
        mock.return_value = expected
        cli = Cli(reader=mock)
        
        actual = cli.prompt_user()

        self.assertEqual(expected, actual)

    def test_prompt_user_2(self):
        mock = Mock()
        expected = "9"
        args = "Some prompt"
        mock.return_value = expected
        cli = Cli(reader=mock)

        actual = cli.prompt_user(args)
        
        mock.assert_called_once_with(args)
        self.assertEqual(expected, actual)

    def test_non_numeric_input(self):
        reader_mock = Mock()
        reader_mock.side_effect = ["invalid input", "1"]
        expected_args = "It seems you may have entered some invalid input. Please try again:\n"
        expected_return = "1"
        cli = Cli(reader=reader_mock)

        actual = cli.prompt_user()

        reader_mock.assert_called_with(expected_args)
        self.assertEqual(expected_return, actual)

    def test_validate_input(self):
        args = "invalid input"
        expected = False
        cli = Cli()

        actual = cli.validate_input(args)

        self.assertEqual(expected, actual)

    def test_input_recursion(self):
        reader_mock = Mock()
        reader_mock.side_effect = ["invalid input"] * 15
        expected = 5
        expected_return = None
        cli = Cli(reader=reader_mock)

        actual_return = cli.prompt_user()
        actual = reader_mock.call_count

        self.assertEqual(expected, actual)
        self.assertEqual(expected_return, actual_return)

    def test_display_empty_board(self):
        board = Board()
        mock = Mock()
        cli = Cli(mock)

        expected =  """
⊱ –––––– {⋆⌘⋆} –––––– ⊰

         |   |   
      ---+---+---
         |   |   
      ---+---+---
         |   |   

⊱ –––––– {⋆⌘⋆} –––––– ⊰
"""

        self.assertEqual(expected, cli.display_board(board))

    def test_display_board_in_progress(self):
        board = Board()
        mock = Mock()
        cli = Cli(mock)
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

        self.assertEqual(expected, cli.display_board(board))

    def test_handle_exit(self):
        mock = Mock()
        cli = Cli(writer=mock)
        expected = "Leaving so soon? Hope to see you back again shortly!"

        cli.handle_exit()

        mock.assert_called_with(expected)
