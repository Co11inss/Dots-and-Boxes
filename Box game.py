
#Constant variables that are used throughout the code
GAPH = " "
GAPV = " "


NUMGAP = 4
       

DASHEDH = "-" #4
DASHEDV = "|"
DASHED = [DASHEDH, DASHEDV]

DOUBLEH = "="
DOUBLEV = "║" #4
DOUBLE = [DOUBLEH, DOUBLEV]


HORIZONTAL_1ST = [0,1]
VERTICAL_1ST = [2,3,4]
HORIZONTAL_2ND = [5,6]
VERTICAL_2ND = [7,8,9]
HORIZONTAL_3RD = [10,11]



def instructions():

    """Displays game instructions"""

    print(
        """
    \nWelcome!

You will make your move known by entering the position of
where you would like to place your dashes

Here are the positions:


                          
        .  0  .  1  .
        2     3     4
        .  5  .  6  .
        7     8     9
        . 10  . 11  .


Not too hard is it?


P.S. Whoever goes first will use normal dashed lines whereas
whoever goes second will use double dashed lines.

P.P.S I bet £5 PLAYER 1 is going to win...)

    """)


def question(question, choice1, choice2):
    """Will be used to ask who's going first (P1/P2)"""
    answer = None
    while answer not in [choice1, choice2]:
        answer = input(question).lower()
    return answer

def ask_number(question, low, high):
    """Ask for a number within a range"""
    answer = None
    while answer not in range(low, high):
        answer = int(input(question))
    return answer



def pieces():
    """Determines the pieces based on the answer from the first question"""
    answer = question("Who's going first? P1 or P2?: ", "p1", "p2")
    if answer ==  "p1":
        P1 = DASHED
        P2 = DOUBLE
        print("Okay... so PLAYER 1 will go first!")
    else:
        P2 = DASHED
        P1 = DOUBLE
        print("Okay... so PLAYER 2 will go first!")
    return P1, P2




def new_board():
    """Creates a new game board"""
    rows = [[],[],[],[],[],[],[],[],[],[],[]]
    rows[0] = [".", GAPH, GAPH, GAPH, GAPH, ".", GAPH, GAPH, GAPH, GAPH, "."]
    rows[1] = [GAPV, GAPH, GAPH, GAPH, GAPH, GAPV, GAPH, GAPH, GAPH, GAPH, GAPV]
    rows[2] = [GAPV, GAPH, GAPH, GAPH, GAPH, GAPV, GAPH, GAPH, GAPH, GAPH, GAPV]
    rows[3] = [GAPV, GAPH, GAPH, GAPH, GAPH, GAPV, GAPH, GAPH, GAPH, GAPH, GAPV]
    rows[4] = [GAPV, GAPH, GAPH, GAPH, GAPH, GAPV, GAPH, GAPH, GAPH, GAPH, GAPV]
    rows[5] = [".", GAPH, GAPH, GAPH, GAPH, ".", GAPH, GAPH, GAPH, GAPH, "."]
    rows[6] = [GAPV, GAPH, GAPH, GAPH, GAPH, GAPV, GAPH, GAPH, GAPH, GAPH, GAPV]
    rows[7] = [GAPV, GAPH, GAPH, GAPH, GAPH, GAPV, GAPH, GAPH, GAPH, GAPH, GAPV]
    rows[8] = [GAPV, GAPH, GAPH, GAPH, GAPH, GAPV, GAPH, GAPH, GAPH, GAPH, GAPV]
    rows[9] = [GAPV, GAPH, GAPH, GAPH, GAPH, GAPV, GAPH, GAPH, GAPH, GAPH, GAPV]
    rows[10] = [".", GAPH, GAPH, GAPH, GAPH, ".", GAPH, GAPH, GAPH, GAPH, "."]
   
    
    return rows

def display_board(rows):
    """Displays the board on the screen"""
    num = 0
    while num < 11:
        print(" ".join(rows[num]))
        num += 1
    


def legal_moves(rows):
    """Creates a list of legal moves"""
    positions  = []
    for row in range(len(rows)):
        for gap in range(len(rows[row])):
            if rows[row][gap] == GAPH or rows[row][gap] == GAPV:
                positions.append(gap)
        return positions





def p1_move(rows, player):
    """Get the player's move"""
    print("\nPLAYER 1's go!\n")
    legal = legal_moves(rows)
    position = None
    while position not in legal:
        position = ask_number("Where would you like to place your dash?(0 - 11): ", 0, 12)
        print("Here you go...\n")
        return position

def p2_move(rows, player):
    """Get the player's move"""
    print("\nPLAYER 2's go!\n")
    legal = legal_moves(rows)
    position = None
    while position not in legal:
        position = ask_number("Where would you like to place your dash?(0 - 11): ", 0, 12)
        print("Here you go...\n")
        return position



def winner(rows, boxcheck):
    """Determine the game winner"""

    #check box 1
    if (boxcheck[0] == 1 and boxcheck[2] == 1 and boxcheck[3] == 1 and boxcheck[5] == 1):
        for i in range(1, 5):
            rows[i][i] = "\\"
        rows[1][4] = "/"
        rows[2][3] = "/"
        rows[3][2] = "/"
        rows[4][1] = "/"
        winner = "WINNER"
        return winner

    #check box 2
    elif (boxcheck[1] == 1 and boxcheck[3] == 1 and boxcheck[4] == 1 and boxcheck[6] == 1): 
        winner = "WINNER"
        for i in range(1,5):
            rows[i][i+5] = "\\"
        rows[1][9] = "/"
        rows[2][8] = "/"
        rows[3][7] = "/"
        rows[4][6] = "/"
        return winner

    #check box 3
    elif (boxcheck[5] == 1 and boxcheck[7] == 1 and boxcheck[8] == 1 and boxcheck[10] == 1): 
        winner = "WINNER"
        for i in range(6,10):
            rows[i][i-5] = "\\"
        rows[6][4] = "/"
        rows[7][3] = "/"
        rows[8][2] = "/"
        rows[9][1] = "/"
        return winner

    #check box 4
    elif (boxcheck[6] == 1 and boxcheck[8] == 1 and boxcheck[9] == 1 and boxcheck[11] == 1):
        winner = "WINNER"
        for i in range(6,10):
            rows[i][i] = "\\"
        rows[6][9] = "/"
        rows[7][8] = "/"
        rows[8][7] = "/"
        rows[9][6] = "/"
        return winner


    return None


def turn_switch(turn):
    """Switch turns."""
    if turn == DASHED:
        return DOUBLE
    else:
        return DASHED


def main():
    instructions()
    P1, P2 = pieces()
    turn = DASHED
    rows = new_board()
    print("")
    display_board(rows)
    print("")

    boxcheck = [0,0,0,0,0,0,0,0,0,0,0,0]
    

    while not winner(rows, boxcheck):
        
        if turn == P1:
            position = p1_move(rows, P1)
            if boxcheck[position] == 0:
                boxcheck[position] = 1
            
            
                if position in HORIZONTAL_1ST:
                    rows[0][1 + HORIZONTAL_1ST.index(position)*5:5 + HORIZONTAL_1ST.index(position)*5] = P1[0]*NUMGAP

                if position in VERTICAL_1ST:
                    for i in range (1,5):
                        rows[i][VERTICAL_1ST.index(position)*5] = P1[1]
                    
                
                if position in HORIZONTAL_2ND:
                    rows[5][1 + HORIZONTAL_2ND.index(position)*5:5 + HORIZONTAL_2ND.index(position)*5] = P1[0]*NUMGAP

                if position in VERTICAL_2ND:
                    for i in range (6,10):
                        rows[i][VERTICAL_2ND.index(position)*5] = P1[1]

                if position in HORIZONTAL_3RD:
                    rows[10][1 + HORIZONTAL_3RD.index(position)*5:5 + HORIZONTAL_3RD.index(position)*5] = P1[0]*NUMGAP

                if winner(rows, boxcheck) == "WINNER":
                    print("\n\tPLAYER 1 has won!\n")
                    print("Congrats Player 1!")
                    print("I knew PLAYER 1 was going to win!\n")
            else:
                print("That position is occupied! Choose again!")
                continue
        else:
            position = p2_move(rows, P2)
            if boxcheck[position] == 0:
                boxcheck[position] = 1
            
                if position in HORIZONTAL_1ST:
                    rows[0][1 + HORIZONTAL_1ST.index(position)*5:5 + HORIZONTAL_1ST.index(position)*5] = P2[0]*NUMGAP

                if position in VERTICAL_1ST:
                    for i in range(1,5):
                        rows[i][VERTICAL_1ST.index(position)*5] = P2[1]

                if position in HORIZONTAL_2ND:
                    rows[5][1 + HORIZONTAL_2ND.index(position)*5:5 + HORIZONTAL_2ND.index(position)*5] = P2[0]*NUMGAP

                if position in VERTICAL_2ND:
                    for i in range(6,10):
                        rows[i][VERTICAL_2ND.index(position)*5] = P2[1]

                if position in HORIZONTAL_3RD:
                    rows[10][1 + HORIZONTAL_3RD.index(position)*5:5 + HORIZONTAL_3RD.index(position)*5] = P2[0]*NUMGAP

                if winner(rows, boxcheck) == "WINNER":
                    print("\n\tPLAYER 2 has won!\n")
                    print("Congrats Player 2")
                    print("Damn... there goes my £5...\n")

            else:
                print("That position is occupied! Choose again!")
                continue
                

        display_board(rows)
        turn = turn_switch(turn)

    the_winner = winner(rows, boxcheck)
    

choice = None

while choice != "0":
    print("""
            \nWelcome to Dots and Boxes

            0 - Exit
            1 - Play""")
    
            
    choice = input("Choice: ")
    

    if choice == "0":
        print("Goodbye!")
        break

    elif choice == "1":
        main()


        
    
    





