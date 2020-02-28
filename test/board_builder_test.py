import unittest

from src.board_builder import BoardBuilder

class BoardBuilderTest(unittest.TestCase):
    def test_setup_3x3_board(self):
        builder = BoardBuilder()
        board_type = BoardBuilder.THREE_BY_THREE
        expected = board_type 

        board = builder.build_board(board_type)
        actual = board.type
        
        self.assertEqual(expected, actual)
