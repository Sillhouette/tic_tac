import unittest
import src.constants as constants

from src.three_by_three_presenter import ThreeByThreePresenter
from src.three_by_three_board import ThreeByThreeBoard

class ThreeByThreePresenterTest(unittest.TestCase):
    
    def test_present_empty_board(self):
        board = ThreeByThreeBoard()
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
        board = ThreeByThreeBoard()
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

