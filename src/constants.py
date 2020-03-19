EXIT = "exit"
WELCOME = "welcome"
CATS = "finished"
ERROR = "error"
OPTION_ERROR = "option error"
WIN = "win"
MOVE = "move"
REQUEST_MOVE = "request"
THREE_BY_THREE = "3x3"
THREE_DIMENSIONAL = "3d"
REPLAY = "replay"
EMPTY_INDEX_COLOR_START = "\u001b[38;5;243m"
EMPTY_INDEX_COLOR_END = "\u001b[0m"
COMPUTER_TURN = "computer_turn"
HARD = "hard"
EASY = "easy"
PLAYER = "player"
OPPONENTS = {
    PLAYER: "Player - Play against another player",
    EASY: "Easy Computer - play against an easy computer",
    HARD: "Hard Computer - play against a hard computer"
}
BOARD_CHOICES = [THREE_BY_THREE, THREE_DIMENSIONAL]
THREE_BY_THREE_WIN_COMBINATIONS = {
    "Top Row": [0, 1, 2],
    "Middle Row": [3, 4, 5],
    "Bottom Row": [6, 7, 8],
    "First Column": [0, 3, 6],
    "Second Column": [1, 4, 7],
    "Third Column": [2, 5, 8],
    "Left to Right Diagonal": [0, 4, 8],
    "Right to Left Diagonal": [2, 4, 6]
}
THREE_DIMENSIONAL_WIN_COMBINATIONS = {
    "First Top Row": [0, 1, 2],
    "First Middle Row": [3, 4, 5],
    "First Bottom Row": [6, 7, 8],
    "First Column": [0, 3, 6],
    "First Second Column": [1, 4, 7],
    "First Third Column": [2, 5, 8],
    "First Left to Right Diagonal": [0, 4, 8],
    "First Right to Left Diagonal": [2, 4, 6],
    "Second Top Row": [9, 10, 11],
    "Second Middle Row": [12, 13, 14],
    "Second Bottom Row": [15, 16, 17],
    "Second Column": [9, 12, 15],
    "Second Second Column": [10, 13, 16],
    "Second Third Column": [11, 14, 17],
    "Second Left to Right Diagonal": [9, 13, 17],
    "Second Right to Left Diagonal": [11, 13, 16],
    "Third Top Row": [18, 19, 20],
    "Third Middle Row": [21, 22, 23],
    "Third Bottom Row": [24, 25, 26],
    "Third Column": [18, 21, 24],
    "Third Second Column": [19, 22, 25],
    "Third Third Column": [20, 23, 26],
    "Third Left to Right Diagonal": [18, 22, 26],
    "Third Right to Left Diagonal": [20, 22, 24],
    "Top To Bottom Back Left": [0, 9, 18],
    "Top To Bottom Back Center": [1, 10, 19],
    "Top To Bottom Back Right": [2, 11, 20],
    "Top To Bottom Middle Left": [3, 12, 21],
    "Top To Bottom Middle Center": [4, 13, 22],
    "Top To Bottom Middle Right": [5, 14, 23],
    "Top To Bottom Front Left": [6, 15, 24],
    "Top To Bottom Front Center": [7, 16, 25],
    "Top To Bottom Front Right": [8, 17, 26],
    "Right Side Back To Front Diagonal": [2, 14, 26],
    "Right Side Front To Back Diagonal": [8, 14, 20],
    "Left Side Back To Front Diagonal": [0, 12, 24],
    "Left Side Front To Back Diagonal": [6, 12, 18],
    "Center Back To Front Diagonal": [1, 13, 25],
    "Center Front To Back Diagonal": [7, 13, 19],
    "Front Left To Right Diagonal": [6, 16, 26],
    "Front Right To Left Diagonal": [8, 16, 24],
    "Middle Left to Right Diagonal": [3, 13, 23],
    "Middle Right To Left Diagonal": [5, 13, 21],
    "Back Left To Right Diagonal": [0, 10, 20],
    "Back Right To Left Diagonal": [2, 10, 18], 
    "Back Left To Front Right Diagonal": [0, 13, 26],
    "Back Right To Front Left Diagonal": [2, 13, 24],
    "Front Left To Back Right Diagonal": [6, 13, 20],
    "Front Right To Back Left Diagonal": [8, 13, 18]
}

