import src.constants as constants

from src.three_by_three_processor import ThreeByThreeProcessor

class ProcessorBuilder():
    def build_processor(self, board):
        if board.type == constants.THREE_BY_THREE:
            return ThreeByThreeProcessor(board)
