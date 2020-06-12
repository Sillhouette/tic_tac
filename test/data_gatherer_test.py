import unittest
import src.constants as constants

from unittest.mock import Mock
from src.data_gatherer import DataGatherer
from src.human_player import HumanPlayer
from src.processor import Processor
from src.board import Board
from src.cli import Cli

class DataGathererTest(unittest.TestCase):
    def test_gather_3x3_info_sets_minimax_attribute_of_gatherer(self):
        gatherer = DataGatherer()
        not_expected = None

        gatherer.gather_3x3_info()
        actual = gatherer.minimax

        self.assertNotEqual(not_expected, actual)
    
    def test_gather_3x3_info_sets_minimax_board_to_3x3(self):
        gatherer = DataGatherer()
        expected = constants.THREE_BY_THREE

        gatherer.gather_3x3_info()
        actual = gatherer.minimax.processor.board.type

        self.assertEqual(expected, actual)
    
