import unittest
import src.constants as constants

from src.three_dimensional_presenter import ThreeDimensionalPresenter
from src.board import Board

class ThreeDimensionalPresenterTest(unittest.TestCase):

    def test_colorize_empty_space_index_properly_returns(self):
        presenter = ThreeDimensionalPresenter()
        index = 1
        expected = f"{constants.EMPTY_INDEX_COLOR_START}0{index}{constants.EMPTY_INDEX_COLOR_END}"

        actual = presenter.colorize_empty_space_index(index)

        self.assertEqual(expected, actual)

    def test_scrub_board_returns_properly_scrubbed_empty_board(self):
        presenter = ThreeDimensionalPresenter()
        board = Board(constants.THREE_DIMENSIONAL)
        expected = []
        for index in list(range(1, 28)):
            expected.append(presenter.colorize_empty_space_index(index))
    
        actual = presenter.scrub_board(board)

        self.assertEqual(expected, actual)

    def test_scrub_board_returns_properly_scrubbed_in_progress_board(self):
        presenter = ThreeDimensionalPresenter()
        board = Board(constants.THREE_DIMENSIONAL)
        moves = [0, 3, 6, 2]
        tokens = ["X", "O", "X", "O"]
        for i, move in enumerate(moves):
            board.update(move, tokens[i])

        expected = []
        for index, token in enumerate(board.spaces):
            if token == None:
                expected.append(presenter.colorize_empty_space_index(index + 1))
            else:
                expected.append(" " + token)

        actual = presenter.scrub_board(board)

        self.assertEqual(expected, actual)

