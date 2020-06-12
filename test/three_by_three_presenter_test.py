import unittest
import src.constants as constants

from src.three_by_three_presenter import ThreeByThreePresenter
from src.board import Board

class ThreeByThreePresenterTest(unittest.TestCase):

    def test_colorize_empty_space_index_properly_returns(self):
        presenter = ThreeByThreePresenter()
        index = 1
        expected = f"{constants.EMPTY_INDEX_COLOR_START}{index}{constants.EMPTY_INDEX_COLOR_END}"

        actual = presenter.colorize_empty_space_index(index)

        self.assertEqual(expected, actual)

    def test_scrub_board_returns_properly_scrubbed_empty_board(self):
        presenter = ThreeByThreePresenter()
        board = Board(constants.THREE_BY_THREE)
        expected = []
        for index in list(range(1, 10)):
            expected.append(presenter.colorize_empty_space_index(index))
    
        actual = presenter.scrub_board(board)

        self.assertEqual(expected, actual)

    def test_scrub_board_returns_properly_scrubbed_in_progress_board(self):
        presenter = ThreeByThreePresenter()
        board = Board(constants.THREE_BY_THREE)
        moves = [0, 3, 6, 2]
        tokens = ["X", "O", "X", "O"]
        for i, move in enumerate(moves):
            board.update(move, tokens[i])

        expected = []
        for index, token in enumerate(board.spaces):
            if token == None:
                expected.append(presenter.colorize_empty_space_index(index + 1))
            else:
                expected.append(token)

        actual = presenter.scrub_board(board)

        self.assertEqual(expected, actual)
    
    def test_present_empty_board(self):
        board = Board(constants.THREE_BY_THREE)
        presenter = ThreeByThreePresenter()
        colorize = (lambda i: f"{constants.EMPTY_INDEX_COLOR_START}{i}{constants.EMPTY_INDEX_COLOR_END}")

        expected =  f"""
{presenter.border}

       {colorize(1)} | {colorize(2)} | {colorize(3)} 
      ---+---+---
       {colorize(4)} | {colorize(5)} | {colorize(6)} 
      ---+---+---
       {colorize(7)} | {colorize(8)} | {colorize(9)} 

{presenter.border}
"""
        actual = presenter.present_board(board)

        self.assertEqual(expected, actual)

    def test_present_board_in_progress(self):
        board = Board(constants.THREE_BY_THREE)
        presenter = ThreeByThreePresenter()
        board.spaces = ["X", None, None, "O", None, "X", None, None, "O"]
        colorize = (lambda i: f"{constants.EMPTY_INDEX_COLOR_START}{i}{constants.EMPTY_INDEX_COLOR_END}")

        expected =  f"""
{presenter.border}

       X | {colorize(2)} | {colorize(3)} 
      ---+---+---
       O | {colorize(5)} | X 
      ---+---+---
       {colorize(7)} | {colorize(8)} | O 

{presenter.border}
"""
        actual = presenter.present_board(board)
        
        self.assertEqual(expected, actual)

