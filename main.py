import os, copy, random
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

def valid_response(response,valid_options,error_message="Invalid input. Please try again."):
    if response in valid_options:
        return True
    else:
        print(error_message)
        return False
    
def get_input(prompt, valid_options):
    while True:
        response = input(prompt)
        if valid_response(response, valid_options, "Invalid input. Please enter one of the following: " + ", ".join(valid_options)):
            return response.upper()

def get_input_num(prompt, valid_options):
    while True:
        response = int(input(prompt))
        if valid_response(response, valid_options, "Invalid input. Please enter a number from the following: " + ", ".join(map(str, valid_options))):
            return response

def update_board(move:int, symbol:str):
    #os.system("clear")
    global GAME_BOARD
    global MOVES_REMAINING
    GAME_BOARD = GAME_BOARD.replace(str(move), symbol)
    print(GAME_BOARD)
    MOVES_REMAINING.remove(int(move))
    print(f"{symbol} was placed in position {move}.")

def computer_move(computer_symbol):
    # Placeholder for computer move logic
    random_move = random.choice(MOVES_REMAINING)
    update_board(random_move, computer_symbol)

def check_win():
    # Placeholder for win checking logic
    pass

def check_draw():
    return True if not WHO_WON["have_won"] and len(MOVES_REMAINING) == 0 else False

def reset_game():
    global GAME_BOARD
    global MOVES_REMAINING
    global WHO_WON
    GAME_BOARD = copy.deepcopy(START_BOARD)
    MOVES_REMAINING = copy.deepcopy(VALID_MOVES)
    WHO_WON = {"have_won": False, "winner": None}

def main():
    first_player = None
    player_turn = None
    while True:
        global START_OF_GAME
        if START_OF_GAME:
            player_symbol = start_game()
            if player_symbol.upper() == "X":
                computer_symbol = "O"
            else:
                computer_symbol = "X"
            first_player = "Player" if player_symbol.upper() == "X" else "Computer"
            print(f"{first_player} will go first.")
            if first_player == "Player":
                print(GAME_BOARD)
                move = (get_input_num(f"Enter your move ({MOVES_REMAINING}): ", MOVES_REMAINING))
                update_board(move, player_symbol)
                player_turn = False
            else:
                computer_move(computer_symbol)
                player_turn = True
            START_OF_GAME = False

        #core game loop
        if check_draw():
            print("It's a draw!")
            print(GAME_BOARD)
            print("Restarting the game...")
            START_OF_GAME = True
            reset_game()
        else:
            if player_turn:
                move = (get_input_num(f"Enter your move ({MOVES_REMAINING}): ", MOVES_REMAINING))
                update_board(move, player_symbol)
                player_turn = False
            else:
                computer_move(computer_symbol)
                player_turn = True
            
            if check_win():
                print(f"{WHO_WON['winner']} has won the game!")


if __name__ == "__main__":
    main()