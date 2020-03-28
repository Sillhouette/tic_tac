[![Build Status](https://travis-ci.org/Sillhouette/tic_tac.svg?branch=master)](https://travis-ci.org/Sillhouette/tic_tac)

# Tic-Tac by Toenails Inc

This is a Tic-Tac-Toe App that includes a normal 3x3 tic-tac-toe mode, a 3-dimensional tic-tac-toe mode, and the ability to play vs other players, an easy computer, and a hard computer. It utilizes a depth limited minimax formula for the hard computer with alpha beta pruning and caches the hard computer's moves for faster games as games are played. 

## Installation:

Follow these easy steps to install and start the app:

### Github:

#### Install:

Clone this repository, change directories into the folder for the repo and run

#### Execute:

You can run the data gatherer to gather the optimal moves for the 3x3 board by running the command `python3 run_data_gatherer.py`. This takes less than 10 minutes. Running this gatherer for a 3-dimensional board is time-prohibited as it takes far too long to solve the game, this is why I've implemented caching as games are played.

Start the application with `python3 run_game.py` You can then select which players you want to play as well as the board type.

#### Test

Run the test suite using the command 'python3 -m unittest _test_runner.py -v'

Thank you!

Austin Melchior

_This project has been licensed under the MIT open source license._
