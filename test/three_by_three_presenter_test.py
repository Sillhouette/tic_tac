import unittest

from src.three_by_three_presenter import ThreeByThreePresenter
from src.three_by_three_board import ThreeByThreeBoard

class ThreeByThreePresenterTest(unittest.TestCase):
    
    def test_present_empty_board(self):
        board = ThreeByThreeBoard()
        presenter = ThreeByThreePresenter()

        expected =  """
⊱ –––––– {⋆⌘⋆} –––––– ⊰

         |   |   
      ---+---+---
         |   |   
      ---+---+---
         |   |   

⊱ –––––– {⋆⌘⋆} –––––– ⊰
"""
        actual = presenter.present_board(board)

        self.assertEqual(expected, actual)

    def test_present_board_in_progress(self):
        board = ThreeByThreeBoard()
        board.spaces = ["X", " ", " ", "O", " ", "X", " ", " ", "O"]
        presenter = ThreeByThreePresenter()
       
        expected = """
⊱ –––––– {⋆⌘⋆} –––––– ⊰

       X |   |   
      ---+---+---
       O |   | X 
      ---+---+---
         |   | O 

⊱ –––––– {⋆⌘⋆} –––––– ⊰
"""
        actual = presenter.present_board(board)
        
        self.assertEqual(expected, actual)

