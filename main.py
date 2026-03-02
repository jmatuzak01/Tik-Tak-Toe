import os, copy
os.system("clear")
START_OF_GAME = True
VALID_MOVES = [int(i) for i in range(1, 10)]
VALID_SYMBOLS = ["X", "O", "x", "o"]
MOVES_REMAINING = copy.deepcopy(VALID_MOVES)
START_BOARD = "|1|2|3|\n|4|5|6|\n|7|8|9|"
GAME_BOARD = "|1|2|3|\n|4|5|6|\n|7|8|9|"

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
    GAME_BOARD = GAME_BOARD.replace(str(move), symbol)
    print(GAME_BOARD)
    print(f"{symbol} was placed in position {move}.")

def computer_move():
    # Placeholder for computer move logic
    pass

def main():
    global START_OF_GAME
    if START_OF_GAME:
        player_symbol = start_game()
        if player_symbol == "X":
            computer_symbol = "O"
        else:
            computer_symbol = "X"
    START_OF_GAME = False
    print(player_symbol)
    
    #move = get_input("Enter your move (1-9): ", valid_moves)
    #updated_board = update_board(GAME_BOARD, move, player_symbol)
    #print("\nUpdated board:")
    #print(updated_board)

if __name__ == "__main__":
    main()