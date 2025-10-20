import sys # To quit the app

# This prints the board to the console
def draw_board(spots):
    board = (f"|{spots[1]}||{spots[2]}||{spots[3]}|\n|{spots[4]}||{spots[5]}||{spots[6]}|\n|{spots[7]}||{spots[8]}||{spots[9]}|")
    print(board)

# Keep track of which turn it is
def check_turn(turn):
    if turn % 2 == 0:   return "O"
    else:   return "X"

def stop_game(turn):
    player = check_turn(turn)  # Gets who the current player is
    print(f"{player} has won!")
    sys.exit() # Quits the game

# Checks available win slots
# Returns true if a player has won and returns false if a player has not won
def check_winner(spots, turn):
    if spots[1] == spots[2] == spots[3] or spots[4] == spots[5] == spots[6] or spots[7] == spots[8] == spots[9]:
        stop_game(turn)
        return True
    elif spots[1] == spots[4] == spots[7] or spots[2] == spots[5] == spots[8] or spots[3] == spots[6] == spots[9]:
        stop_game(turn)
        return True
    elif spots[3] == spots[5] == spots[7] or spots[1] == spots[5] == spots[9]:
        stop_game(turn)
        return True
    else:
        return False


def check_tie(spots, turn):
    winning = check_winner(spots, turn) # Checks if player has won or not
    # Checks for a tie
    if turn >= 9 and winning == False:
        print("tie")
        sys.exit()
