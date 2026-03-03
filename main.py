import os, copy
os.system("clear")
START_OF_GAME = True
VALID_MOVES = [int(i) for i in range(1, 10)]
VALID_SYMBOLS = ["X", "O", "x", "o"]
MOVES_REMAINING = copy.deepcopy(VALID_MOVES)
START_BOARD = "|1|2|3|\n|4|5|6|\n|7|8|9|"
GAME_BOARD = "|1|2|3|\n|4|5|6|\n|7|8|9|"
WHO_WON = {"have_won": False, "winner": None}

def start_game():
    print("Welcome to Tic Tac Toe!")
    player_symbol_choice = get_input("Choose your symbol (X/O): ", VALID_SYMBOLS)
    print(f"You have chosen {player_symbol_choice}. The computer will be {'O' if player_symbol_choice == 'X' else 'X'}.")
    return player_symbol_choice

def valid_response(response,valid_options):
    if response in valid_options:
        return True
    else:
        print("Invalid input. Please try again.")
        return False
    
def get_input(prompt, valid_options):
    while True:
        response = input(prompt)
        if valid_response(response, valid_options):
            return response.upper()

def update_board(move, symbol):
    os.system("clear")
    global GAME_BOARD
    global MOVES_REMAINING
    GAME_BOARD = GAME_BOARD.replace(str(move), symbol)
    print(GAME_BOARD)
    MOVES_REMAINING.remove(int(move))
    print(f"{symbol} was placed in position {move}.")

def computer_move(computer_symbol):
    # Placeholder for computer move logic
    pass

def check_win():
    # Placeholder for win checking logic
    pass

def main():
    global START_OF_GAME
    if START_OF_GAME:
        player_symbol = start_game()
        if player_symbol == "X":
            computer_symbol = "O"
        else:
            computer_symbol = "X"
        first_player = "Player" if player_symbol == "X" else "Computer"
        print(f"{first_player} will go first.")
        START_OF_GAME = False
    if first_player == "Player":
        move = get_input(f"Enter your move ({MOVES_REMAINING}): ", MOVES_REMAINING)
        update_board(move, player_symbol)
    else:
        computer_move(computer_symbol)
    check_win()
    if WHO_WON["have_won"]:
        print(f"{WHO_WON['winner']} has won the game!")


if __name__ == "__main__":
    main()