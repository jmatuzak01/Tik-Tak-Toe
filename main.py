import os, copy, random
os.system("clear")
START_OF_GAME = True
VALID_MOVES = [int(i) for i in range(1, 10)]
MOVES_REMAINING = copy.deepcopy(VALID_MOVES)
COMPUTER_MOVE = {"move": 0, "score": 0}
VALID_SYMBOLS = ["X", "O", "x", "o"]
START_BOARD = [
    ['1', '2', '3'],
    ['4', '5', '6'],
    ['7', '8', '9']]
GAME_BOARD = [
    ['1', '2', '3'],
    ['4', '5', '6'],
    ['7', '8', '9']]
WHO_WON = {"have_won": False, "winner": None}
TURN_COUNTER: int = 1

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
        try:
            response = int(input(prompt))
            if valid_response(response, valid_options, "Invalid input. Please enter a number " + "(".join(map(str, valid_options)) + ")"):
                return response
        except ValueError:
            print("Invalid input. Please enter a number.")

def format_board(board):
    formatted_board = ""
    for row in board:
        formatted_board += " | ".join(row) + "\n"
    return formatted_board

def update_board(move:int, symbol:str, board=None, is_temp:bool=False):
    global TURN_COUNTER, MOVES_REMAINING
    if board is None:
        board = GAME_BOARD
    for row in board:
        for i in range(len(row)):
            if row[i] == str(move):
                row[i] = symbol
    if not is_temp:
        print(format_board(board))
        MOVES_REMAINING.remove(int(move))
        print(f"{symbol} was placed in position {move}.")
        TURN_COUNTER += 1

def computer_move(computer_symbol:str, player_symbol:str):
    # Priority 1: win if possible
    for move in MOVES_REMAINING:
        temp_board = copy.deepcopy(GAME_BOARD)
        update_board(move, computer_symbol, temp_board, is_temp=True)
        if check_win(computer_symbol, temp_board):
            update_board(move, computer_symbol)
            return

    # Priority 2: block player from winning
    for move in MOVES_REMAINING:
        temp_board = copy.deepcopy(GAME_BOARD)
        update_board(move, player_symbol, temp_board, is_temp=True)
        if check_win(player_symbol, temp_board):
            update_board(move, computer_symbol)
            return

    # Priority 3: fallback to random
    update_board(random.choice(MOVES_REMAINING), computer_symbol)

def check_win_row(symbol,board):
    global WHO_WON
    for row in board:
        if len(set(row)) == 1 and row[0] == symbol:
            if board is GAME_BOARD:
                set_winner(row[0])
            return True
    return False

def check_win_column(symbol,board):
    global WHO_WON
    for i in range(len(board[0])):
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] == symbol:
            if board is GAME_BOARD:
                set_winner(board[0][i])
            return True
    return False

def check_win_diagonal(symbol,board):
    global WHO_WON
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] == symbol:
        if board is GAME_BOARD:
            set_winner(board[0][0])
        return True
    elif board[0][2] == board[1][1] == board[2][0] and board[0][2] == symbol:
        if board is GAME_BOARD:
            set_winner(board[0][2])
        return True
    return False

def set_winner(winner):
    global WHO_WON
    WHO_WON["have_won"] = True
    WHO_WON["winner"] = winner

def check_win(symbol:str, board=None):
    if board is None:
        board = GAME_BOARD
    return check_win_row(symbol, board) or check_win_column(symbol, board) or check_win_diagonal(symbol, board)

def check_draw():
    return True if not WHO_WON["have_won"] and len(MOVES_REMAINING) == 0 else False

def reset_game():
    global GAME_BOARD, START_OF_GAME, MOVES_REMAINING, WHO_WON, TURN_COUNTER
    GAME_BOARD = copy.deepcopy(START_BOARD)
    MOVES_REMAINING = copy.deepcopy(VALID_MOVES)
    WHO_WON = {"have_won": False, "winner": None}
    START_OF_GAME = True
    TURN_COUNTER = 1
    os.system("clear")

def end_of_game(player_symbol:str, computer_symbol:str):
    global WHO_WON
    if check_win(player_symbol):
        print("You won!")
        WHO_WON["have_won"] = True
        WHO_WON["winner"] = player_symbol
    elif check_win(computer_symbol):
        print("Computer won!")
        WHO_WON["have_won"] = True
        WHO_WON["winner"] = computer_symbol
    elif check_draw():
        print("It's a draw!")
        WHO_WON["have_won"] = True
        WHO_WON["winner"] = None
    if WHO_WON["have_won"]:
        input("Press any key to play again...")
        reset_game()
        return True
    return False
    
def main():
    first_player = None
    player_turn = None
    global START_OF_GAME, TURN_COUNTER, WHO_WON
    while True:
        if START_OF_GAME:
            player_symbol = start_game()
            if player_symbol.upper() == "X":
                computer_symbol = "O"
            else:
                computer_symbol = "X"
            first_player = "Player" if player_symbol.upper() == "X" else "Computer"
            print(f"{first_player} will go first.")
            if first_player == "Player":
                print(format_board(GAME_BOARD))
                move = (get_input_num(f"Enter your move ({MOVES_REMAINING}): ", MOVES_REMAINING))
                update_board(move, player_symbol)
                player_turn = False
            else:
                computer_move(computer_symbol, player_symbol)
                player_turn = True
            START_OF_GAME = False
            continue

        # core game loop
        else:
            if end_of_game(player_symbol, computer_symbol):
                continue
            if player_turn:
                move = get_input_num(f"Enter your move ({MOVES_REMAINING}): ", MOVES_REMAINING)
                update_board(move, player_symbol)
                player_turn = False
                if end_of_game(player_symbol, computer_symbol):
                    continue
            else:
                computer_move(computer_symbol, player_symbol)
                player_turn = True
                if end_of_game(player_symbol, computer_symbol):
                    continue

if __name__ == "__main__":
    main()