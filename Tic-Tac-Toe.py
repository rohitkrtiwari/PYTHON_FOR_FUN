def sum(a, b, c ):
    return a + b + c

def valAllowed(val, xState, yState):
    if(val>8 or val<0):
        print("value out of range")
        return 0
    elif(xState[val] == 1 or yState[val] == 1):
        print("This Position is already Played!")
        return 0
    return 1
    pass

def Board(xState, yState):
    val = []
    for i in range(9):
        temp = 'X' if xState[i] else ('O' if yState[i] else i)
        val.append(temp)
    
    print(f"{val[0]} | {val[1]} | {val[2]} ")
    print(f"--|---|---")
    print(f"{val[3]} | {val[4]} | {val[5]} ")
    print(f"--|---|---")
    print(f"{val[6]} | {val[7]} | {val[8]} ")

def checkWin(xState, yState):
    wins = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for win in wins:
        if( (xState[win[0]] + xState[win[1]] + xState[win[2]]) == 3):
            print("\nX Won the match")
            return 1
        if( (yState[win[0]] + yState[win[1]] + yState[win[2]]) == 3):
            print("O Won the match")
            return 0
    return -1


if __name__ == '__main__':
    xState = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    yState = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    turn = 1
    print("Welcome to Tick Tack Toe Game!")
    while(True):
        Board(xState, yState)
        if(turn == 1):
            print("X's Chance: ")
            value = int(input("Please enter a value: "))
            vAllowed = valAllowed(value, xState, yState)
            if(not vAllowed):
                continue
            xState[value] = 1
        else :
            print("Y's Chance")
            value = int(input("Please enter a value: "))
            vAllowed = valAllowed(value, xState, yState)
            if(not vAllowed):
                continue
            yState[value] = 1
        cwin = checkWin(xState, yState) 
        if( cwin !=-1):
            break
        turn = 1 - turn
