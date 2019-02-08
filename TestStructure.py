









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
print("\n\n\n")


print("Index\t", end='')

for z in range(2 * size + 1):
    print(z,"\t", end='')

print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

dotDash = 1
NewLineOffSet = 1
BOARD_POSITION = []
for x in range(2 * size + 1):
    BOARD_POSITION.append([])
    print(" ", x, "]\t", end='')
    for y in range (2 * size + 1):
        dotDash = 1
        if NewLineOffSet % 2 != 0:
            BOARD_POSITION[x].append(".")
            if x % 2 == 0:
                print(" . \t", end='')
            else:
                print("  \t", end='')
            dotDash += 1
        else:
            BOARD_POSITION[x].append(dotDash)
            print(y, "\t", end='')
            dotDash += 1
        NewLineOffSet += 1
    print("\n")

