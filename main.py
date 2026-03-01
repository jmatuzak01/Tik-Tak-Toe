import os, copy
os.system("clear")
valid_moves = [int(i) for i in range(1, 10)]
moves_remaining = copy.deepcopy(valid_moves)

def valid_response(response,valid_options=["X", "O", "x", "o"]):
    if response in valid_options:
        return True
    else:
        print("Invalid input. Please try again.")
        return False
print(f"valid moves: {valid_moves}")

player_symbol = input("Enter your symbol (X or O): ").upper()

while not valid_response(player_symbol):
    player_symbol = input("Enter your symbol (X or O): ").upper()
print(f"You chose: {player_symbol}")

line1 = "|1|2|3|"
line2 = "|4|5|6|"
line3 = "|7|8|9|"
print("\n".join([line1, line2, line3]))
def get_player_move(moves_remaining):
   while True:
    try:
        input_move = int(input(f"Choose a number to place your {player_symbol}.\nValid moves are {min(moves_remaining)} to {max(moves_remaining)}: "))
        if input_move in moves_remaining:
            return input_move
    except ValueError:
        print("Invalid input. Please enter a number.")
player_move = get_player_move(moves_remaining)
print(f"You chose move: {player_move}")