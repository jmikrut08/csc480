from colorama import Fore
import random

# random score generator and array



BOX_SCORES = [] # multidimensional array that keeps score of each square generated
GAME_BOARD = [] # Multidimensional array that stores edges
MOVE_TABLE = [] # multidimensional table of moves done.
COORDINATES = []
EDGES = [] #  list of edges/moves
MOVES_LEFT = [] # range of numbers of edges left in game board
FULL_SQUARES = [] # list of completed squares
USER_SCORE = 0
COMP_SCORE = 0
CHOSEN_DEPTH = 0
# EDGE_KEY_COUNTER = 1
BOX_KEY_COUNTER = 1
CHILD_KEY_COUNTER = 1
# NAME_LETTERS = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
PLAYER_ONE = 1 # red
PLAYER_TWO = 2 # blue
CURRENT_PLAYER = 1
CHILDREN = [] # stores child nodes in terminal group



class Coordinate:
    verticalIndex = 0
    horizontalIndex = 0

    def __init__(self, vertIn, horIn):
        self.verticalIndex = vertIn
        self.horizontalIndex = horIn

    def getVertIndex(self):
        return self.verticalIndex

    def getHorIndex(self):
        return self.horizontalIndex

class Edge:
    key = 0
    pt1 = 0
    pt2 = 0
    player = 0

    def __init__(self, keyIn, row, index, player):
        self.key = keyIn
        self.pt1 = row
        self.pt2 = index
        self.player = player

class Square:
    key = 0
    edge1 = 0
    edge2 = 0
    edge3 = 0
    edge4 = 0
    points = 0
    user = 0

    def __init__(self, key, edge1Key, edge2Key, edge3Key, edge4Key, points, user):
        self.key = key
        self.edge1 = edge1Key
        self.edge2 = edge2Key
        self.edge3 = edge3Key
        self.edge4 = edge4Key
        self.points = points
        self.user = user

def getPlayer():
    global CURRENT_PLAYER
    return CURRENT_PLAYER

def addMove(key):
    global GAME_BOARD
    global MOVES_LEFT
    for row in GAME_BOARD:
        for col in row:
            if col == key:
                if key in MOVES_LEFT:
                    rowIndex = GAME_BOARD.index(row)
                    colIndex = row.index(col)
                    edge = Edge(key, rowIndex, colIndex, getPlayer())
                    global EDGES
                    EDGES.append(edge)
                    MOVES_LEFT.remove(key)
                    global MOVE_TABLE
                    MOVE_TABLE[rowIndex][colIndex] = getPlayer()
                    changePlayer()


def isMoveAvailable(int):
    global MOVES_LEFT
    for x in MOVES_LEFT:
        if x == int:
            return True
    return False

def isIndexAvailable(x, y):
    global MOVE_TABLE
    if MOVE_TABLE[x][y] > 0:
        return True
    else:
        return False

def changePlayer():
    global CURRENT_PLAYER
    global PLAYER_ONE
    global PLAYER_TWO
    if CURRENT_PLAYER == PLAYER_ONE:
        CURRENT_PLAYER = 2
        return
    else:
        CURRENT_PLAYER = 1

def createBoardIndex(size):
    NewLineOffSet = 1
    BOARD_POSITION = []
    for x in range(2 * size + 1):
        BOARD_POSITION.append([])
        for y in range(2 * size + 1):
            dotDash = 1
            if NewLineOffSet % 2 != 0:
                BOARD_POSITION[x].append(".")
                if x % 2 == 0:
                    print(".\t", end='')
                else:
                    print("\t", end='')
                dotDash += 1
            else:
                BOARD_POSITION[x].append(dotDash)
                print(y, "\t", end='')
                dotDash += 1
            NewLineOffSet += 1
        print("\n")

def createBoard(size):
    dotDash = 1
    NewLineOffSet = 1
    global GAME_BOARD
    global MOVE_TABLE
    GAME_BOARD = []
    MOVE_TABLE = []
    for x in range(2 * size + 1):
        GAME_BOARD.append([])
        MOVE_TABLE.append([])
        for y in range (2 * size + 1):
            if NewLineOffSet % 2 != 0:
                if x % 2 == 0:
                    print(Fore.RESET, "+".center(5), end='')
                    coordinate = Coordinate(x,y)
                    global COORDINATES
                    COORDINATES.append(coordinate)
                    GAME_BOARD[x].append(0)
                    MOVE_TABLE[x].append(0)
                else:
                    GAME_BOARD[x].append(random.randint(1,5))
                    MOVE_TABLE[x].append(0)
                    print(Fore.CYAN, str(GAME_BOARD[x][y]).center(5), end='')
            else:
                GAME_BOARD[x].append(dotDash)
                MOVE_TABLE[x].append(0)
                print(Fore.RESET, '{:^5d}'.format(dotDash), end="")
                dotDash += 1
            NewLineOffSet += 1
        print("\n")
    global MOVES_LEFT
    MOVES_LEFT = list(range(1, int(GAME_BOARD[-1][-2]) + 1))

def printGameBoard():
    global GAME_BOARD
    global MOVES_LEFT
    dot = "+"
    vertDash = "|"
    horDash = "--"
    for x in GAME_BOARD:
        for y in x:
            if y == 0: # prints dots
                print(Fore.RESET, '{:^5s}'.format(dot), end="")
                continue
            if GAME_BOARD.index(x) % 2 != 0:
                if x.index(y) % 2 != 0:
                    print(Fore.CYAN, '{:^5d}'.format(y), end="") # prints box points
                else: # prints vertical edges
                    # global MOVES_LEFT
                    if y in MOVES_LEFT:
                        print(Fore.RESET, '{:^5d}'.format(y), end="") # prints unplayed vertical edges
                    else:
                        print(Fore.BLUE, '{:^5s}'.format(vertDash), end="") # prints played vertical edges
            else: # prints horizontal edges
                #global MOVES_LEFT
                if y in MOVES_LEFT:
                    print(Fore.RESET, '{:^5d}'.format(y), end="") # prints unplayed horizontal edges
                else:
                    print(Fore.BLUE, '{:^5s}'.format(horDash), end="")  # prints played vertical edges
        print("\n")

def numberOfSides(edgeKey):
    global GAME_BOARD
    global MOVE_TABLE
    global BOX_KEY_COUNTER
    global FULL_SQUARES
    boxBelow = []
    boxAbove = []
    boxRight = []
    boxLeft = []
    if isMoveAvailable(edgeKey):
        coordinates = getCoordinates(edgeKey)
        row = coordinates[0]
        col = coordinates[1]
        if row == 0: #boxBelow
            if MOVE_TABLE[row+1][col-1] > 0:
                coordinates = [ row+1, col-1 ]
                boxBelow.append(coordinates)
            if MOVE_TABLE[row+1][col+1] > 0:
                coordinates = [ row+1, col+1 ]
                boxBelow.append(coordinates)
            if MOVE_TABLE[row+2][col] > 0:
                coordinates = [ row+2, col ]
                boxBelow.append(coordinates)
        if col == 0: #boxRight
            if MOVE_TABLE[row-1][col+1] > 0:
                coordinates = [ row-1, col+1 ]
                boxRight.append(coordinates)
            if MOVE_TABLE[row][col+2] > 0:
                coordinates = [ row, col+2 ]
                boxRight.append(coordinates)
            if MOVE_TABLE[row+1][col+1] > 0:
                coordinates = [ row+1, col+1 ]
                boxRight.append(coordinates)
        if row == (len(GAME_BOARD)-1): #boxAbove
            if MOVE_TABLE[row-1][col-1] > 0:
                coordinates = [ row-1, col-1 ]
                boxAbove.append(coordinates)
            if MOVE_TABLE[row-1][col+1] > 0:
                coordinates = [ row-1, col+1 ]
                boxAbove.append(coordinates)
            if MOVE_TABLE[row-2][col] > 0:
                coordinates = [ row-2, col ]
                boxAbove.append(coordinates)
        if col == (len(GAME_BOARD)-1): #boxLEFT
            if MOVE_TABLE[row-1][col-1] > 0:
                coordinates = [row-1, col-1]
                boxLeft.append(coordinates)
            if MOVE_TABLE[row][col-2] > 0:
                coordinates = [row, col-2]
                boxLeft.append(coordinates)
            if MOVE_TABLE[row+1][col-1] > 0:
                coordinates = [row+1, col-1]
                boxLeft.append(coordinates)
        if row % 2 != 0 and col > 0 and col < (len(GAME_BOARD)-1): # checks Left and Right Boxes
            # left
            if MOVE_TABLE[row-1][col-1] > 0:
                coordinates = [row-1, col-1]
                boxLeft.append(coordinates)
            if MOVE_TABLE[row][col-2] > 0:
                coordinates = [row, col-2]
                boxLeft.append(coordinates)
            if MOVE_TABLE[row+1][col-1] > 0:
                coordinates = [row+1, col-1]
                boxLeft.append(coordinates)
            # right
            if MOVE_TABLE[row-1][col+1] > 0:
                coordinates = [ row-1, col+1 ]
                boxRight.append(coordinates)
            if MOVE_TABLE[row][col+2] > 0:
                coordinates = [ row, col+2 ]
                boxRight.append(coordinates)
            if MOVE_TABLE[row+1][col+1] > 0:
                coordinates = [ row+1, col+1 ]
                boxRight.append(coordinates)
        if row % 2 == 0 and row > 0 and row < (len(GAME_BOARD)-1):
            # below
            if MOVE_TABLE[row+1][col-1] > 0:
                coordinates = [ row+1, col-1 ]
                boxBelow.append(coordinates)
            if MOVE_TABLE[row+1][col+1] > 0:
                coordinates = [ row+1, col+1 ]
                boxBelow.append(coordinates)
            if MOVE_TABLE[row+2][col] > 0:
                coordinates = [ row+2, col ]
                boxBelow.append(coordinates)
            # above
            if MOVE_TABLE[row-1][col-1] > 0:
                coordinates = [ row-1, col-1 ]
                boxAbove.append(coordinates)
            if MOVE_TABLE[row-1][col+1] > 0:
                coordinates = [ row-1, col+1 ]
                boxAbove.append(coordinates)
            if MOVE_TABLE[row-2][col] > 0:
                coordinates = [ row-2, col ]
                boxAbove.append(coordinates)
        if len(boxBelow) == 3:
            belowCompleted = Square(BOX_KEY_COUNTER, GAME_BOARD[row][col], GAME_BOARD[boxBelow[0][0]][boxBelow[0][1]],
                    GAME_BOARD[boxBelow[1][0]][boxBelow[1][1]], GAME_BOARD[boxBelow[2][0]][boxBelow[2][1]], GAME_BOARD[row+1][col],
                    getPlayer())
            FULL_SQUARES.append(belowCompleted)
            BOX_KEY_COUNTER += 1
        if len(boxAbove) == 3:
            aboveCompleted = Square(BOX_KEY_COUNTER, GAME_BOARD[row][col], GAME_BOARD[boxAbove[0][0]][boxAbove[0][1]],
                    GAME_BOARD[boxAbove[1][0]][boxAbove[1][1]], GAME_BOARD[boxAbove[2][0]][boxAbove[2][1]], GAME_BOARD[row-1][col],
                    getPlayer())
            FULL_SQUARES.append(aboveCompleted)
            BOX_KEY_COUNTER += 1
        if len(boxRight) == 3:
            rightCompleted = Square(BOX_KEY_COUNTER, GAME_BOARD[row][col], GAME_BOARD[boxRight[0][0]][boxRight[0][1]],
                    GAME_BOARD[boxRight[1][0]][boxRight[1][1]], GAME_BOARD[boxRight[2][0]][boxRight[2][1]], GAME_BOARD[row][col+1],
                    getPlayer())
            FULL_SQUARES.append(rightCompleted)
            BOX_KEY_COUNTER += 1
        if len(boxLeft) == 3:
            leftCompleted = Square(BOX_KEY_COUNTER, GAME_BOARD[row][col], GAME_BOARD[boxLeft[0][0]][boxLeft[0][1]],
                    GAME_BOARD[boxLeft[1][0]][boxLeft[1][1]], GAME_BOARD[boxLeft[2][0]][boxLeft[2][1]], GAME_BOARD[row][col-1],
                    getPlayer())
            FULL_SQUARES.append(leftCompleted)
            BOX_KEY_COUNTER += 1

def getCoordinates(edgeKey):
    global GAME_BOARD
    coordinates = []
    for x in GAME_BOARD:
        for y in x:
            if y == edgeKey:
                row = GAME_BOARD.index(x)
                col = GAME_BOARD[row].index(y)
                if row % 2 != 0 and col % 2 != 0:
                    continue
                else:
                    coordinates.append(row)
                    coordinates.append(col)
                    print(coordinates)
                    return coordinates


###################################################################
#------------------ MINIMAX STUFF STARTS HERE -------------------#
###################################################################

class Child:
    key = 0
    type = "" # max or min node
    state = []
    parentKey = 0
    parentState = []
    childKeys = []
    childStates = []
    move = 0
    points = 0
    alpha = 0
    beta = 0
    depth = 0
    totalPoints = 0

    def __init__(self, key, state, type, parentKey, parentState, move, points, depth):
        self.key = key
        self.state = state
        self.type = type
        self.parentKey = parentKey
        self.parentState = parentState
        self.move = move
        self.points = points
        self.depth = depth


    def getKey(self):
        return self.key

    def getState(self):
        return self.state

    def getParentKey(self):
        return self.parentKey

    def getParentState(self):
        return self.parentState

    def getMove(self):
        return self.move

    def getPoints(self):
        return self.points

    def getTotalPoints(self):
        return self.totalPoints

    def getDepth(self):
        return self.depth

    def getType(self):
        return self.type

    def getChildren(self):
        return self.childStates

    def setAlpha(self, points):
        self.alpha = points

    def setBeta(self, points):
        self.beta = points

    def setMove(self, edgeKey):
        self.move = edgeKey

    def setTotalPoints(self, points):
        self.totalPoints += points

    def addChildNode(self, childNode):
        self.childStates.apppend(childNode)

    def createChildBoard(self):
        global GAME_BOARD
        child = GAME_BOARD.copy()
        return child



def minimax(node, movesLeft, depth,): # create first child outside of minimax algo, before calling it.
    if depth == 0 or len(movesLeft) == 0: # add terminal nodes here too
        return node.getTotalPoints()
    #checks if nodes are max nodes
    if node.getType() == "MAX":
        # make children

        value = -999999


def max(gameBoard, movesLeft, depth):
    if depth == 0 or len(movesLeft) == 0: # add terminal nodes here too
        return gameBoard.getTotalPoints()



def min(gameBoard, movesLeft, depth):
    pass

#RESET CHILD KEY COUNTER BEFORE MINI MAX TO 0
# TOP NODE = Child(CHILD_KEY_COUNTER, GAME_BOARD, "MAX", 0, 0, 0, 0, CHOSEN_DEPTH)
def generateChildren(parentNode, movesleft):
    # def __init__(self, key, state, type, parentKey, parentState, move, points, depth):
    global CHILD_KEY_COUNTER
    listOfChildren = []
    if parentNode.getType() == "MAX":
        for element in movesleft:
            nodeState = parentNode.getState.copy()

            addMove(element)



def addChildMove(key, node, movesleft):
    global GAME_BOARD

    global MOVES_LEFT
    for row in node.getState():
        for col in row:
            if col == key:
                if key in movesleft:
                    rowIndex = node.getState.index(row)
                    colIndex = row.index(col)

                    # add key/edge to gameboard and return node. 

                    # edge = Edge(key, rowIndex, colIndex, getPlayer())
                    # global EDGES
                    # EDGES.append(edge)
                   # MOVES_LEFT.remove(key)
                    # global MOVE_TABLE
                    # MOVE_TABLE[rowIndex][colIndex] = getPlayer()
                    # changePlayer()
                    return node


#BoardSize = input("What Size Board Do You Want To Use?\n")
BoardSize = "5"
size = int(BoardSize)
BOARD = []
createBoardIndex(size)
print("\n\n\n")
createBoard(size)
print("\n\n")
for x in GAME_BOARD:
    print(x)

print(Fore.RED + 'some red text')
print(Fore.BLUE + 'some red text')
print(Fore.GREEN + 'some red text')

print(MOVES_LEFT)
print(isMoveAvailable(60))
# for x in COORDINATES:
#     print("[{}][{}]".format(x.getVertIndex(), x.getHorIndex()))

printGameBoard()

#addMove(14)
#addMove(6)
addMove(45)
addMove(56)
addMove(51)
numberOfSides(50)
addMove(50)
#numberOfSides(14)

print("\n\n\n")

printGameBoard()

print(MOVES_LEFT)

for x in MOVE_TABLE:
    print(x)

print(FULL_SQUARES)
# dotDash = 1
# EdgeNum = 1
# for x in range(2 * size + 1):
#     BOARD.append([])
#     for y in range (2 * size + 1):
#         if dotDash % 2 != 0:
#             BOARD[x].append(".")
#             print("o\t", end='')
#         else:
#             BOARD[x].append(EdgeNum)
#             print(EdgeNum, "\t", end='')
#             EdgeNum += 1
#         dotDash += 1
#     print("\n")
# print("\n\n\n")


#print("Index\t", end='')

#for z in range(2 * size + 1):
 #   print(z,"\t", end='')

#print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
# ACTUAL PRINT FOR GAMEBOARD
# dotDash = 1
# NewLineOffSet = 1
# BOARD_POSITION = []
# for x in range(2 * size + 1):
#     BOARD_POSITION.append([])
#     # print(" ", x, "]\t", end='')
#     for y in range (2 * size + 1):
#         #dotDash = 1
#         if NewLineOffSet % 2 != 0:
#             BOARD_POSITION[x].append(".")
#             if x % 2 == 0:
#                 print("o\t", end='')
#             else:
#                 print("  \t", end='')
#             # dotDash += 1
#         else:
#             BOARD_POSITION[x].append(dotDash)
#             print(dotDash, "\t", end='')
#             dotDash += 1
#         NewLineOffSet += 1
#     print("\n")



# SizeOfBoard = input("What Size of Board do you want?")

# PRINT BOARD WITH INDEXES
# dotDash = 1
# NewLineOffSet = 1
# BOARD_POSITION = []
# for x in range(2 * size + 1):
#     BOARD_POSITION.append([])
#     for y in range (2 * size + 1):
#         dotDash = 1
#         if NewLineOffSet % 2 != 0:
#             BOARD_POSITION[x].append(".")
#             if x % 2 == 0:
#                 print(".\t", end='')
#             else:
#                 print("\t", end='')
#             dotDash += 1
#         else:
#             BOARD_POSITION[x].append(dotDash)
#             print(y, "\t", end='')
#             dotDash += 1
#         NewLineOffSet += 1
#     print("\n")