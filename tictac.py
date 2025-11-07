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

    if pos == 1 and a1 not in ['X','O']: a1 = symbol; return True
    elif pos == 2 and a2 not in ['X','O']: a2 = symbol; return True
    elif pos == 3 and a3 not in ['X','O']: a3 = symbol; return True
    elif pos == 4 and a4 not in ['X','O']: a4 = symbol; return True
    elif pos == 5 and a5 not in ['X','O']: a5 = symbol; return True
    elif pos == 6 and a6 not in ['X','O']: a6 = symbol; return True
    elif pos == 7 and a7 not in ['X','O']: a7 = symbol; return True
    elif pos == 8 and a8 not in ['X','O']: a8 = symbol; return True
    elif pos == 9 and a9 not in ['X','O']: a9 = symbol; return True
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
    if pos not in [1,2,3,4,5,6,7,8,9]:
        return False
    cell_values = [a1,a2,a3,a4,a5,a6,a7,a8,a9]
    return cell_values[pos-1] not in ['X','O']

turn = "X"
moves = 0

while True:
    Print_board()
    print("Player", turn, "turn")
    
    try:
        pos = int(input("Enter position (1-9): "))
    except ValueError:
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
