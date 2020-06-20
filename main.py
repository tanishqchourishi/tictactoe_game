
# ----------------Global Variable------------------

#game board
board=["-","-","-",
       "-","-","-",
       "-","-","-",]

#if game is still going
game_still_going= True

#who won?
winner = None

# whos turn is it
current_player="X"


#display board
def display_board():
    print(board[0]+" | "+board[1]+" | "+board[2])
    print(board[3]+" | "+board[4]+" | "+board[5])    
    print(board[6]+" | "+board[7]+" | "+board[8])
    
def play_game():
    # Display initial board
    display_board()
    

    #while the game is still going
    while game_still_going:
        handle_turn(current_player)
        check_if_game_over()
        flip_player()
    # game has ended
    if winner=="X" or winner=="O":
        print(winner +" Won.")
    elif winner==None:
        print("Tie.")



#check if game has ended
def check_if_game_over():
    check_if_win()
    check_if_tie()

def check_if_win():
    #setup global winner
    global winner

    #check rows
    row_winner=check_rows()
    #check columns
    column_winner=check_columns()
    #check diagonals
    diagonal_winner=check_diagonals()


    if row_winner:
        #there was a win
        winner=row_winner
    elif column_winner:
        #thers was a column winner
        winner=column_winner
    elif diagonal_winner:
        #there was a diagonal winner
        winner=diagonal_winner
    else:
        winner=None

    return

def check_rows():
    # sset up global variables
    global game_still_going
    # check if any rows have the same valuues
    row1=board[0]==board[1]==board[2]!="-"
    row2=board[3]==board[4]==board[5]!="-"
    row3=board[6]==board[7]==board[8]!="-"
    #if any one of them is true,then game is over
    if row1 or row2 or row3:
        game_still_going=False
    if row1:
        return board[0]
    elif row2:
        return board[3]
    elif row3:
        return board[6]

    
    return
def check_columns():
     # sset up global variables
    global game_still_going
    # check if any columns have the same valuues
    colm1=board[0]==board[3]==board[6]!="-"
    colm2=board[1]==board[4]==board[7]!="-"
    colm3=board[2]==board[5]==board[8]!="-"
    #if any one of them is true,then game is over
    if colm1 or colm2 or colm3:
        game_still_going=False
    if colm1:
        return board[0]
    elif colm2:
        return board[1]
    elif colm3:
        return board[2]
    return
def check_diagonals():
    global game_still_going
    # check if any diagonals have the same valuues
    diagonal1=board[0]==board[4]==board[8]!="-"
    diagonal2=board[2]==board[4]==board[6]!="-"
    
    #if any one of them is true,then game is over
    if diagonal1 or diagonal2 :
        game_still_going=False
        return board[4]
    
    return

#flip to other person
def flip_player():
    global current_player
    if current_player=="X":
        current_player="O"
    elif current_player=="O":
        current_player="X"
    return

def check_if_tie():
    global game_still_going
    if "-" not in board:
        game_still_going=False
    return


#handle a single turn of an arbitrary player
def handle_turn(player):
    print(player+ "'s turn.")

    position=input("choose a position from 1-9:")
    valid= False
    while not valid:
        while position not in ["1","2","3","4","5","6","7","8","9"]:
            position=input("Inavalid Input.Choose a position from 1-9:")
        position=int(position)-1 # we are eventually asking for the entry in a list
        if board[position] == "-":
            valid=True
        else:    
            print("you can't go there.Go again")
   
    board[position]=player
    
    display_board()

play_game()

