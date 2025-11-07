a1, a2, a3 = 1, 2, 3
a4, a5, a6 = 4, 5, 6
a7, a8, a9 = 7, 8, 9

def Print_board():
    print(" "," "," ","*"," "," "," ","*"," "," "," ")
    print(" ",a1," ","*"," ",a2," ","*"," ",a3," ")
    print(" "," "," ","*"," "," "," ","*"," "," "," ")
    print("*","*","*","*","*","*","*","*","*","*","*") 
    print(" "," "," ","*"," "," "," ","*"," "," "," ")
    print(" ",a4," ","*"," ",a5," ","*"," ",a6," ")
    print(" "," "," ","*"," "," "," ","*"," "," "," ")
    print("*","*","*","*","*","*","*","*","*","*","*")
    print(" "," "," ","*"," "," "," ","*"," "," "," ")
    print(" ",a7," ","*"," ",a8," ","*"," ",a9," ")
    print(" "," "," ","*"," "," "," ","*"," "," "," ")

def update(pos, symbol):
    global a1,a2,a3,a4,a5,a6,a7,a8,a9

    if pos == 1 : a1 = symbol; return True
    elif pos == 2 : a2 = symbol; return True
    elif pos == 3: a3 = symbol; return True
    elif pos == 4 : a4 = symbol; return True
    elif pos == 5 : a5 = symbol; return True
    elif pos == 6 : a6 = symbol; return True
    elif pos == 7 : a7 = symbol; return True
    elif pos == 8 : a8 = symbol; return True
    elif pos == 9 : a9 = symbol; return True
    else:
        return False

def winner(symbol):
    if (a1==a2==a3==symbol or a4==a5==a6==symbol or a7==a8==a9==symbol or
        a1==a4==a7==symbol or a2==a5==a8==symbol or a3==a6==a9==symbol or
        a1==a5==a9==symbol or a3==a5==a7==symbol):
        return True
    else:
        return False

def check(pos):
    if pos < 1 or pos > 9:
        return False  # invalid position number
    
    if pos == 1 and a1 not in ['X','O']: return True
    if pos == 2 and a2 not in ['X','O']: return True
    if pos == 3 and a3 not in ['X','O']: return True
    if pos == 4 and a4 not in ['X','O']: return True
    if pos == 5 and a5 not in ['X','O']: return True
    if pos == 6 and a6 not in ['X','O']: return True
    if pos == 7 and a7 not in ['X','O']: return True
    if pos == 8 and a8 not in ['X','O']: return True
    if pos == 9 and a9 not in ['X','O']: return True

    return False 

turn = "X"
moves = 0

while True:
    Print_board()
    print("Player", turn, "turn")
    pos = int(input("Enter position (1-9): "))
    if check(pos)==False:
        print("Invalid input! Enter a number between 1 and 9.")
        continue

    if not check(pos):
        print("Invalid move! Try again.")
        continue

    update(pos, turn)
    moves += 1

    if winner(turn):
        Print_board()
        print("Player", turn, "wins!")
        break

    if moves == 9:
        Print_board()
        print("Game Draw!")
        break

    # switch turns
    turn = "O" if turn == "X" else "X"