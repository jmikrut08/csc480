









BoardSize = input("What Size Board Do You Want To Use?\n")
size = int(BoardSize)
BOARD = []
print("\n\n\n")
dotDash = 1
EdgeNum = 1
for x in range(2 * size + 1):
    BOARD.append([])
    for y in range (2 * size + 1):
        if dotDash % 2 != 0:
            BOARD[x].append(".")
            print("o\t", end='')
        else:
            BOARD[x].append(EdgeNum)
            print(EdgeNum, "\t", end='')
            EdgeNum += 1
        dotDash += 1
    print("\n")
    # print(BOARD[x])
    # print("calculating")
# print(BOARD)


