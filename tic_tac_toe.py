# In this script you can write your code.
# Start by writing all the functions.
# In the last part after if __name__ == "__main__": you can call the functions to play your game.
# If you run `python tic_tac_toe.py` in the command line the game will start. Try it out! ;)

# 
board_list = [["_", "_", "_"],
              ["_", "_", "_"],
              ["_", "_", "_"]]

# Function for displaying the board
def board(game):
    #for row in board:
    for row in game:
        print (row)


# board(board_list)
def test_win(game, symbol): # 
    win = False

    # Test horizontal
    for row in game:
        if row.count(symbol) == 3: # One row
            win = True
            break

    # Test Vertical
    for col in range(0,3):
        column = [game[0][col], game[1][col], game[2][col]]
        if column.count(symbol) == 3:
            win = True
            break

    # Test Diagonal
    diag_1 = [game[0][0], game[1][1], game[2][2]]
    diag_2 = [game[0][2], game[1][1], game[2][0]]
    if diag_1.count(symbol) == 3:
        win = True
    elif diag_2.count(symbol) == 3:
        win = True

    return win


# While loop for the turns
def match_round(game):
    # Greeting
    print("Welcome to a new round of Tic-Tac-Toe!")
    player1=input("What's your name, Player 1? ") ### Should be accessible to the loop steps?
    player2=input("What's your name, Player 2? ")
    print(f"Match between {player1} and {player2}! Let's GET READY TO TICTACTOEEEE!!")
    print ("This is your gameboard. Three rows and three columns.")
    board (game)
    print ("Each round you will be asked to give me a row first: 1, 2 or 3. And then a column: 1, 2, 3.")

    # Function for testing the validity of row and cell numbers    
    def valid_number(v, row_or_col):
        while v not in [1,2,3]:
            v = int(input(f"{player} Choose a {row_or_col} from 1 to 3: "))
            if v in [1,2,3]:
                return v
            else:       
                print("Choose a valid number from 1 to 3")
    
    count = 1
    while count <= 9:
        if count % 2 != 0:
            player = player1
            symbol = "X"
        else:
            player = player2
            symbol = "O"
        
        # Ask for the row number and test wether it is in 1:3
        x = 0
        x = valid_number(x,"row")

        # Ask for a column number and test if in 1:3     
        y = 0
        y = valid_number(y,"column")
        
        #  make a useful index of x and y
        x -= 1
        y -= 1
        # Check if the position is already taken.
        if game[x][y] in ("X", "O"): # is taken
            print ("This position is already filled. Choose again!")
            continue
        
        # Cell not taken, assign the players symbol to the cell
        game[x][y] = symbol

        # Print the new board
        board (game)

        # Test wether the current player has won and exit the while loop with Congratulations printed
        if test_win(game, symbol):
            print(f"Congrats {player} - you have won the Game of DEATH!!!")
            break
        
        count += 1

    # While loop fully finished - board full - No winner
    if count == 10:
        print("It's a draw. Try again next time...")

# Tic-tac-toe game
if __name__ == "__main__": 
    match_round(board_list)

#    # Start a new round of Tic-tac-toe
#    print("Welcome to a new round of Tic-Tac-Toe!")
