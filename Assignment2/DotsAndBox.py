from colorama import Fore
import random
import copy

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
CHOSEN_DEPTH = 4
# EDGE_KEY_COUNTER = 1
BOX_KEY_COUNTER = 1
CHILD_KEY_COUNTER = 1
CHILDREN = []
# NAME_LETTERS = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
PLAYER_ONE = 1 # red
PLAYER_TWO = 2 # blue ALWAYS COMPUTER
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

    def getPoints(self):
        return self.points

def getPlayer():
    global CURRENT_PLAYER
    return CURRENT_PLAYER

def addMove(key):
    global GAME_BOARD
    global MOVES_LEFT
    print(MOVES_LEFT)
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
                    print(MOVES_LEFT)
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

def numberOfSides(edgeKey, moveTable):
    global GAME_BOARD
    # global MOVE_TABLE
    global BOX_KEY_COUNTER
    global FULL_SQUARES
    points = 0
    boxBelow = []
    boxAbove = []
    boxRight = []
    boxLeft = []
    if isMoveAvailable(edgeKey):
        coordinates = getCoordinates(edgeKey)
        row = coordinates[0]
        col = coordinates[1]
        if row == 0: #boxBelow
            if moveTable[row+1][col-1] > 0:
                coordinates = [ row+1, col-1 ]
                boxBelow.append(coordinates)
            if moveTable[row+1][col+1] > 0:
                coordinates = [ row+1, col+1 ]
                boxBelow.append(coordinates)
            if moveTable[row+2][col] > 0:
                coordinates = [ row+2, col ]
                boxBelow.append(coordinates)
        if col == 0: #boxRight
            if moveTable[row-1][col+1] > 0:
                coordinates = [ row-1, col+1 ]
                boxRight.append(coordinates)
            if moveTable[row][col+2] > 0:
                coordinates = [ row, col+2 ]
                boxRight.append(coordinates)
            if moveTable[row+1][col+1] > 0:
                coordinates = [ row+1, col+1 ]
                boxRight.append(coordinates)
        if row == (len(GAME_BOARD)-1): #boxAbove
            if moveTable[row-1][col-1] > 0:
                coordinates = [ row-1, col-1 ]
                boxAbove.append(coordinates)
            if moveTable[row-1][col+1] > 0:
                coordinates = [ row-1, col+1 ]
                boxAbove.append(coordinates)
            if moveTable[row-2][col] > 0:
                coordinates = [ row-2, col ]
                boxAbove.append(coordinates)
        if col == (len(GAME_BOARD)-1): #boxLEFT
            if moveTable[row-1][col-1] > 0:
                coordinates = [row-1, col-1]
                boxLeft.append(coordinates)
            if moveTable[row][col-2] > 0:
                coordinates = [row, col-2]
                boxLeft.append(coordinates)
            if moveTable[row+1][col-1] > 0:
                coordinates = [row+1, col-1]
                boxLeft.append(coordinates)
        if row % 2 != 0 and col > 0 and col < (len(GAME_BOARD)-1): # checks Left and Right Boxes
            # left
            if moveTable[row-1][col-1] > 0:
                coordinates = [row-1, col-1]
                boxLeft.append(coordinates)
            if moveTable[row][col-2] > 0:
                coordinates = [row, col-2]
                boxLeft.append(coordinates)
            if moveTable[row+1][col-1] > 0:
                coordinates = [row+1, col-1]
                boxLeft.append(coordinates)
            # right
            if moveTable[row-1][col+1] > 0:
                coordinates = [ row-1, col+1 ]
                boxRight.append(coordinates)
            if moveTable[row][col+2] > 0:
                coordinates = [ row, col+2 ]
                boxRight.append(coordinates)
            if moveTable[row+1][col+1] > 0:
                coordinates = [ row+1, col+1 ]
                boxRight.append(coordinates)
        if row % 2 == 0 and row > 0 and row < (len(GAME_BOARD)-1):
            # below
            if moveTable[row+1][col-1] > 0:
                coordinates = [ row+1, col-1 ]
                boxBelow.append(coordinates)
            if moveTable[row+1][col+1] > 0:
                coordinates = [ row+1, col+1 ]
                boxBelow.append(coordinates)
            if moveTable[row+2][col] > 0:
                coordinates = [ row+2, col ]
                boxBelow.append(coordinates)
            # above
            if moveTable[row-1][col-1] > 0:
                coordinates = [ row-1, col-1 ]
                boxAbove.append(coordinates)
            if moveTable[row-1][col+1] > 0:
                coordinates = [ row-1, col+1 ]
                boxAbove.append(coordinates)
            if moveTable[row-2][col] > 0:
                coordinates = [ row-2, col ]
                boxAbove.append(coordinates)
        if len(boxBelow) == 3:
            belowCompleted = Square(BOX_KEY_COUNTER, GAME_BOARD[row][col], GAME_BOARD[boxBelow[0][0]][boxBelow[0][1]],
                    GAME_BOARD[boxBelow[1][0]][boxBelow[1][1]], GAME_BOARD[boxBelow[2][0]][boxBelow[2][1]], GAME_BOARD[row+1][col],
                    getPlayer())
            FULL_SQUARES.append(belowCompleted)
            BOX_KEY_COUNTER += 1
            points += belowCompleted.getPoints()
        if len(boxAbove) == 3:
            aboveCompleted = Square(BOX_KEY_COUNTER, GAME_BOARD[row][col], GAME_BOARD[boxAbove[0][0]][boxAbove[0][1]],
                    GAME_BOARD[boxAbove[1][0]][boxAbove[1][1]], GAME_BOARD[boxAbove[2][0]][boxAbove[2][1]], GAME_BOARD[row-1][col],
                    getPlayer())
            FULL_SQUARES.append(aboveCompleted)
            BOX_KEY_COUNTER += 1
            points += aboveCompleted.getPoints()
        if len(boxRight) == 3:
            rightCompleted = Square(BOX_KEY_COUNTER, GAME_BOARD[row][col], GAME_BOARD[boxRight[0][0]][boxRight[0][1]],
                    GAME_BOARD[boxRight[1][0]][boxRight[1][1]], GAME_BOARD[boxRight[2][0]][boxRight[2][1]], GAME_BOARD[row][col+1],
                    getPlayer())
            FULL_SQUARES.append(rightCompleted)
            BOX_KEY_COUNTER += 1
            points += rightCompleted.getPoints()
        if len(boxLeft) == 3:
            leftCompleted = Square(BOX_KEY_COUNTER, GAME_BOARD[row][col], GAME_BOARD[boxLeft[0][0]][boxLeft[0][1]],
                    GAME_BOARD[boxLeft[1][0]][boxLeft[1][1]], GAME_BOARD[boxLeft[2][0]][boxLeft[2][1]], GAME_BOARD[row][col-1],
                    getPlayer())
            FULL_SQUARES.append(leftCompleted)
            BOX_KEY_COUNTER += 1
            points += leftCompleted.getPoints()
    return points



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
                    #print(coordinates)
                    return coordinates


###################################################################
#------------------ MINIMAX STUFF STARTS HERE -------------------#
###################################################################

class Child:
    key = 0
    type = "" # max or min node
    #state = []
    movesLeft = []
    movesTable = []
    parentKey = 0
    childKeys = []
    childStates = []
    move = 0
    coordinates = []
    points = 0
    alpha = 0
    beta = 0
    depth = 0
    totalPoints = 0

    def __init__(self, key, movesLeft, movesTable, type, parentKey, move, coordinates, points, totalPoints, depth):
        self.key = key
        #self.state = state # game board
        self.movesLeft = movesLeft
        self.movesTable = movesTable
        self.type = type # MAX/MIN
        self.parentKey = parentKey
        self.move = move #edge
        self.coordinates = coordinates
        self.points = points
        self.totalPoints = totalPoints
        self.depth = depth


    def getKey(self):
        return self.key

    # def getState(self):
    #     return self.state

    def getMovesLeft(self):
        return self.movesLeft

    def getMovesTable(self):
        return self.movesTable

    def getParentKey(self):
        return self.parentKey

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

    def addChildKey(self, childNode):
        self.childStates.apppend(childNode)

    # def createChildBoard(self):
    #     global GAME_BOARD
    #     child = GAME_BOARD.copy()
    #     return child


# clear out children before running this CHILDREN.clear()
# def minimax(node, depth,): # create first child outside of minimax algo, before calling it.
#     global CHILD_KEY_COUNTER
#     CHILD_KEY_COUNTER = 0
#     if depth == 0 or len(node.getMovesLeft()) == 0: # add terminal nodes here too
#         return node.getTotalPoints()
#     #checks if nodes are max nodes
#     if node.getType() == "MAX":
#         # make children
#
#         value = -999999
#
#
# def max(node, depth):
#     if depth == 0 or len(node.getMovesLeft()) == 0: # add terminal nodes here too
#         return node.getTotalPoints()
#
#
# def min(gameBoard, movesLeft, depth):
#     pass

#RESET CHILD KEY COUNTER BEFORE MINI MAX TO 0
# TOP NODE = Child(CHILD_KEY_COUNTER, MOVE_TABLE, "MAX", 0, 0, 0, 0, CHOSEN_DEPTH) NEEEEDS TO BE UPDATED
def generateChildren(parentNode):
    # self, key, state, movesLeft, movesTable, type, parentKey, move, coordinates, points, depth):
    global CHILD_KEY_COUNTER
    #global CHILDREN
    listOfChildren = []
    for move in parentNode.getMovesLeft():  # for each move
        #childNodeState = parentNode.getState().copy()  # creates copy of the state of the board
        childMoveTable = copy.deepcopy(parentNode.getMovesTable())  # creates grid of moves
        coordinates = getCoordinates(move)  # returns location of edge on game board
        print(coordinates[0])
        if childMoveTable[coordinates[0]][coordinates[1]] == 0:  # if edge not has been played before
            points = numberOfSides(move, parentNode.getMovesTable())  # checks if this move results in any points
            childMovesLeft = copy.deepcopy(parentNode.getMovesLeft())  # copies list of moves left (avoids points squares and zero values for dots
            childMovesLeft.remove(move)  # removes move from moves left before creation of child node
            # scoring happens in nodes
            if parentNode.getType() == "MAX":  # if this is a max node, make min nodes
                childMoveTable[coordinates[0]][coordinates[1]] = 2
                # key, movesLeft, movesTable, type, parentKey, move, coordinates, points, totalPoints, depth):
                child = Child(CHILD_KEY_COUNTER, childMovesLeft, childMoveTable, "MIN", parentNode.getKey(), move, coordinates, points, (parentNode.getTotalPoints() + points), (copy.deepcopy(parentNode.getDepth())+1))
                listOfChildren.append(child)
            if parentNode.getType() == "MIN": # if this is a min node, make max nodes
                childMoveTable[coordinates[0]][coordinates[1]] = 1
                # key, movesLeft, movesTable, type, parentKey, move, coordinates, points, totalPoints, depth):
                child = Child(CHILD_KEY_COUNTER, childMovesLeft, childMoveTable, "MAX", parentNode.getKey(), move, coordinates, points, (parentNode.getTotalPoints() - points), (copy.deepcopy(parentNode.getDepth())+1))
                listOfChildren.append(child)
            CHILD_KEY_COUNTER += 1
    return listOfChildren

# parentNode = (CHILD_KEY_COUNTER(0), , childMoveTable, "MIN", parentNode.getKey(), move, coordinates, points, (parentNode.getTotalPoints() + points), (parentNode.getDepth()+1))
def minimax(node):
    print(node.getMove(), node.getTotalPoints(), node.getDepth())
    if node.getDepth == (2 * CHOSEN_DEPTH) or (len(node.getMovesLeft()) == 0):
        print("fuckthisshitisawesome")
        return node
    # print(node.getKey())
    if node.getType() == "MAX":
        maxValueNode = node
        listofChildren = generateChildren(node)
        for child in listofChildren:
            valueNode = minimax(child)
            # maxValueNode = max(maxValueNode.getTotalPoints(), valueNode.getTotalPoints())
            print(maxValueNode.getTotalPoints(), valueNode.getTotalPoints())
            if valueNode.getTotalPoints() > maxValueNode.getTotalPoints():
                return valueNode
            else:
                return maxValueNode
    if node.getType() == "MIN":
        minValueNode = node
        listofChildren = generateChildren(node)
        for child in listofChildren:
            valueNode = minimax(child)
            if valueNode.getTotalPoints() > minValueNode.getTotalPoints():
                return valueNode
            else:
                return minValueNode


#BoardSize = input("What Size Board Do You Want To Use?\n")
BoardSize = "2"
size = int(BoardSize)
#BOARD = []
# createBoardIndex(size)
#print("\n\n\n")
createBoard(size)
print("\n\n")
for x in GAME_BOARD:
    print(x)

#key, movesLeft, movesTable, type, parentKey, move, coordinates, points, totalPoints, depth):

node = Child(0, MOVES_LEFT, MOVE_TABLE, "MAX", 0, 0, [], 0, 0, 0)
x = 5
while x > 0:
    print(node.getKey(), node.getMove(), node.getDepth(), node.getType())
    node = minimax(node)
    print(node.getMove())
    addMove(node.getMove())
    #printGameBoard()
    x -= 1

#print(MOVES_LEFT)
#print(isMoveAvailable(60))
# for x in COORDINATES:
#     print("[{}][{}]".format(x.getVertIndex(), x.getHorIndex()))

printGameBoard()

#addMove(45)
#addMove(56)
#addMove(51)
#numberOfSides(50, MOVE_TABLE)
#addMove(50)
#numberOfSides(14)

#print("\n\n\n")

#printGameBoard()

#print(MOVES_LEFT)

