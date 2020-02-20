import unittest

from src.board import Board

class BoardTest(unittest.TestCase):
    def test_empty_board_to_s(self):
       board = Board()
       expected = [ 
            #"⊱ –––––– {⋆⌘⋆} –––––– ⊰",
            "",
            "         |   |   ",
            "      ---+---+---",
            "         |   |   ",
            "      ---+---+---",
            "         |   |   ",
            "",
            #"⊱ –––––– {⋆⌘⋆} –––––– ⊰"
       ]

       self.assertEqual(expected, board.stringify_spaces())

    def test_board_with_pieces(self):
        board = Board()
        board.spaces = ["X", " ", " ", "O", " ", "X", " ", " ", "O"]
        expected = [
            #"⊱ –––––– {⋆⌘⋆} –––––– ⊰",
            "",
            "       X |   |   ",
            "      ---+---+---",
            "       O |   | X ",
            "      ---+---+---",
            "         |   | O ",
            "",
            #"⊱ –––––– {⋆⌘⋆} –––––– ⊰"
        ]

        self.assertEqual(expected, board.stringify_spaces())
