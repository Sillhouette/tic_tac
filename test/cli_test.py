import unittest
import src.constants as constants

from unittest.mock import call, Mock
from src.cli import Cli
from src.board import Board
from src.processor import Processor
from src.three_by_three_presenter import ThreeByThreePresenter

class CliTest(unittest.TestCase):
    def test_log_message_logs_message(self):
        writer = Mock()
        cli = Cli(writer=writer)
        test_string = "Hello World"

        actual = cli.log(test_string)

        writer.assert_called_once_with(test_string)

    def test_set_dependencies_sets_3x3_board_when_given_processor_with_3x3_board(self):
        board = Board(constants.THREE_BY_THREE)
        processor = Processor(board)
        cli = Cli()
        expected = True

        cli.set_dependencies(processor)
        actual = isinstance(cli.presenter, ThreeByThreePresenter)

        self.assertEqual(expected, actual)
 
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
        board = Board(constants.THREE_BY_THREE)
        processor = Processor(board)
        writer = Mock()
        cli = Cli(writer=writer)
        cli.set_dependencies(processor)
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

    def test_print_empty_3x3_board(self):
        board = Board(constants.THREE_BY_THREE)
        processor = Processor(board)
        writer = Mock()
        cli = Cli(writer=writer)
        cli.set_dependencies(processor)
        colorize = (lambda i: f"{constants.EMPTY_INDEX_COLOR_START}{i}{constants.EMPTY_INDEX_COLOR_END}")

        expected =  f"""
{cli.presenter.border}

       {colorize(1)} | {colorize(2)} | {colorize(3)} 
      ---+---+---
       {colorize(4)} | {colorize(5)} | {colorize(6)} 
      ---+---+---
       {colorize(7)} | {colorize(8)} | {colorize(9)} 

{cli.presenter.border}
"""
        actual = cli.print_board(board)

        writer.assert_called_once_with(expected)

    def test_print_3x3_board_in_progress(self):
        board = Board(constants.THREE_BY_THREE)
        processor = Processor(board)
        writer = Mock()
        cli = Cli(writer=writer)
        cli.set_dependencies(processor)
        board.spaces = ["X", None, None, "O", None, "X", None, None, "O"]
        colorize = (lambda i: f"{constants.EMPTY_INDEX_COLOR_START}{i}{constants.EMPTY_INDEX_COLOR_END}")

        expected =  f"""
{cli.presenter.border}

       X | {colorize(2)} | {colorize(3)} 
      ---+---+---
       O | {colorize(5)} | X 
      ---+---+---
       {colorize(7)} | {colorize(8)} | O 

{cli.presenter.border}
"""
        actual = cli.print_board(board)
        
        writer.assert_called_once_with(expected)

    def test_handle_exit(self):
        writer = Mock()
        cli = Cli(writer=writer)
        expected = Cli.MESSAGES[constants.EXIT] 

        actual = cli.handle_exit()

        writer.assert_called_with(expected)
    
    def test_handle_replay(self):
        writer = Mock()
        cli = Cli(writer=writer)
        expected = Cli.MESSAGES[constants.REPLAY]

        actual = cli.handle_replay()

        writer.assert_called_with(expected)


    def test_handle_cats_game(self):
        writer = Mock()
        cli = Cli(writer=writer)
        expected = Cli.MESSAGES[constants.CATS]

        actual = cli.handle_cats_game()

        writer.assert_called_with(expected)

    def test_welcome(self):
        writer = Mock()
        cli = Cli(writer=writer)
        expected = Cli.MESSAGES[constants.WELCOME] 

        actual = cli.welcome()

        writer.assert_called_with(expected)

    def test_notify_for_computer_player(self):
        writer = Mock()
        cli = Cli(writer=writer)
        expected = Cli.MESSAGES[constants.COMPUTER_TURN]

        actual = cli.notify_for_computer_turn()

        writer.assert_called_with(expected)

    def test_invalid_move(self):
        writer = Mock()
        cli = Cli(writer=writer)
        expected = Cli.MESSAGES[constants.ERROR] 

        actual = cli.invalid_move()

        writer.assert_called_with(expected)

 
    def test_get_player_tokens_returns_list_of_player_tokens(self):
        cli = Cli()
        expected = ["X", "O"]
        
        actual = cli.get_player_tokens()

        self.assertEqual(expected, actual)

    def test_get_board_type_returns_1_when_player_chooses_1(self):
        reader = Mock()
        writer = Mock()
        reader.return_value = "1"
        cli = Cli(writer, reader)
        expected = "1"

        actual = cli.get_board_type()

        self.assertEqual(expected, actual)

    def test_generate_opponent_menu(self):
        cli = Cli()
        expected = f"Choose your opponent:\n  1. {constants.OPPONENTS[constants.PLAYER]}\n  2. {constants.OPPONENTS[constants.EASY]}\n  3. {constants.OPPONENTS[constants.HARD]}\n"

        actual = cli.generate_opponent_menu()

        self.assertEqual(expected, actual)

    def test_get_opponent(self):
        reader = Mock()
        cli = Cli(reader=reader)
        prompt = "Choose your opponent:\n"
        player = f"  1. {constants.OPPONENTS[constants.PLAYER]}\n"
        easy = f"  2. {constants.OPPONENTS[constants.EASY]}\n"
        hard = f"  3. {constants.OPPONENTS[constants.HARD]}\n"
        expected = prompt + player + easy + hard

        cli.get_opponent()

        cli.reader.assert_called_with(expected)

    def test_request_move(self):
        player = Mock()
        player.token = "X"
        reader = Mock()
        cli = Cli(reader=reader)
        cli.prompt_user = Mock()
        expected = "It's X's turn! Please select a square using 1-9:\n"

        actual = cli.request_move(player)

        cli.prompt_user.assert_called_with(expected)

    def test_build_possible_results_returns_list_with_all_possible_results(self):
        player_1 = Mock()
        player_2 = Mock()
        player_1.token = "X"
        player_2.token = "O"
        players = [player_1, player_2]
        cli = Cli()
        expected = True

        results = cli.build_possible_results(players)

        results_has_player_1_key = player_1.token in results
        results_has_player_2_key = player_2.token in results
        results_has_exit_key = constants.EXIT in results
        results_has_finished_key = constants.CATS in results

        self.assertEqual(expected, results_has_player_1_key)
        self.assertEqual(expected, results_has_player_2_key)
        self.assertEqual(expected, results_has_exit_key)
        self.assertEqual(expected, results_has_finished_key)

