import random, copy, threading
lock = threading.Lock()

GAME_BOARD = [] # Multidimensional array that stores edges
MOVE_TABLE = [] # multidimensional table of moves done.
MOVES_LEFT = [] # range of numbers of edges left in game board
USER_SCORE = 0 # Player score
COMP_SCORE = 0 # computer score
CHOSEN_DEPTH = 0 # chosen depth that determines number of plys
CHILD_KEY_COUNTER = 1 # bookkeeping just to follow the nodes during debugging.
PLAYER_ONE = 1 # USER mark on move table
PLAYER_TWO = 2 # COMP mark on move table
CURRENT_PLAYER = 1 # changes to signify which player is playing that move for MOVE_TABLE
PLAYED_MOVES = []

def getPlayer():
    global CURRENT_PLAYER
    return CURRENT_PLAYER

# UPDATES MOVE_TABLE AND REMOVES MOVE FROM MOVES_LEFT
def addMove(key):
    global GAME_BOARD
    global MOVES_LEFT
    for row in GAME_BOARD:
        for col in row:
            if col == key:
                if key in MOVES_LEFT:
                    rowIndex = GAME_BOARD.index(row)
                    colIndex = row.index(col)
                    MOVES_LEFT.remove(key)
                    global MOVE_TABLE
                    MOVE_TABLE[rowIndex][colIndex] = getPlayer()
                    changePlayer()

# RETURNS BOOLEAN CHECK FOR IF MOVE IS IN MOVES LEFT
def isMoveAvailable(int):
    global MOVES_LEFT
    for x in MOVES_LEFT:
        if x == int:
            return True
    return False

# CHECKS IF MOVE_TABLE[x][y] HAS BEEN PLAYED YET; RETURNS BOOLEAN
def isIndexAvailable(x, y):
    global MOVE_TABLE
    if MOVE_TABLE[x][y] > 0:
        return True
    else:
        return False

# CHANGES PLAYER AFTER EVERY MOVE. SO MOVE_TABLE IS UPDATED WITH THE PROPER PLAYER INDICATOR
def changePlayer():
    global CURRENT_PLAYER
    global PLAYER_ONE
    global PLAYER_TWO
    if CURRENT_PLAYER == PLAYER_ONE:
        CURRENT_PLAYER = 2
    else:
        CURRENT_PLAYER = 1

# INITIALIZES ORIGINAL GAMEBOARD AFTER DETERMINING DESIRED WIDTH
def createBoard(size):
    global lock
    lock.acquire(True)
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
                    print("+".center(5), end='')
                    GAME_BOARD[x].append(0)
                    MOVE_TABLE[x].append(0)
                else:
                    GAME_BOARD[x].append(random.randint(1,5))
                    MOVE_TABLE[x].append(0)
                    print(str(GAME_BOARD[x][y]).center(5), end='')
            else:
                GAME_BOARD[x].append(dotDash)
                MOVE_TABLE[x].append(0)
                print('{:^5d}'.format(dotDash), end="")
                dotDash += 1
            NewLineOffSet += 1
        print("\n")
    global MOVES_LEFT
    MOVES_LEFT = list(range(1, int(GAME_BOARD[-1][-2]) + 1))
    lock.release()

# PRINTS ALREADY EXISTING GAME BOARD WITH UPDATED MOVES
def printGameBoard():
    global lock
    lock.acquire(True)
    global GAME_BOARD
    global MOVE_TABLE
    dot = "+"
    vertDash = "|"
    horDash = "--"
    xIndex = 0
    for x in GAME_BOARD:
        index = 0
        for y in x:
            if y == 0: # prints dots
                print('{:^5s}'.format(dot), end="")
                continue
            if GAME_BOARD.index(x) % 2 != 0:
                if index % 2 != 0:
                    print('{:^5d}'.format(y), end="") # prints box points
                else: # prints vertical edges
                    # global MOVES_LEFT
                    if y in MOVES_LEFT:
                        print('{:^5d}'.format(y), end="") # prints unplayed vertical edges
                    else:
                        print('{:^5s}'.format(vertDash), end="") # prints played vertical edges
            else: # prints horizontal edges
                #global MOVES_LEFT
                if y in MOVES_LEFT:
                    print('{:^5d}'.format(y), end="") # prints unplayed horizontal edges
                else:
                    print('{:^5s}'.format(horDash), end="")  # prints played vertical edges
            index += 1
        xIndex += 1
        print("\n")
    lock.release()

# SCORE KEEPING. CHECKS IF MOVE COMPLETES A SQUARE AND THEN RETURNS THE POINTS SCORED.
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
            points += GAME_BOARD[row+1][col]
        if len(boxAbove) == 3:
            points += GAME_BOARD[row-1][col]
        if len(boxRight) == 3:
            points += GAME_BOARD[row][col+1]
        if len(boxLeft) == 3:
            points += GAME_BOARD[row][col-1]
    return points

# RETURNS COORDINATES FOR SPECIFIC MOVE KEY
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
                    return coordinates
    return coordinates

###################################################################
#------------------ MINIMAX STUFF STARTS HERE -------------------#
###################################################################

# CLASS FOR CHILDREN GAME STATES.
class Child:
    key = 0 # basic identifier
    type = "" # max or min node
    movesLeft = [] # moves left at the time of this move being played
    movesTable = [] # move locations, used for scoring
    parentKey = 0 # don't really need this.
    childKeys = [] # don't really need this.
    childStates = [] # don't really need this.
    move = 0 # move key
    coordinates = [] # used for scoring. location on move table
    points = 0 # scoring method store
    depth = 0 # ply number.
    totalPoints = 0 # where evaluation function is added to for terminal nodes

    def __init__(self, key, movesLeft, movesTable, type, parentKey, move, coordinates, points, totalPoints, depth):
        self.key = key
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

    def setTotalPoints(self, points):
        self.totalPoints += points


def generateChildren(parentNode):
    global CHILD_KEY_COUNTER
    listOfChildren = []
    for move in parentNode.getMovesLeft():  # for each move
        childMoveTable = copy.deepcopy(parentNode.getMovesTable())  # creates grid of moves
        coordinates = getCoordinates(move)  # returns location of edge on game board
        if len(coordinates) > 0:
            if childMoveTable[coordinates[0]][coordinates[1]] == 0:  # if edge not has been played before
                points = numberOfSides(move, parentNode.getMovesTable())  # checks if this move results in any points
                childMovesLeft = copy.deepcopy(parentNode.getMovesLeft())  # copies list of moves left (avoids points squares and zero values for dots
                childMovesLeft.remove(move)  # removes move from moves left before creation of child node
                # scoring happens in nodes
                if parentNode.getType() == "MAX":  # if this is a max node, make min nodes
                    childMoveTable[coordinates[0]][coordinates[1]] = 2 # updates MOVE_TABLE for child - used for scoring.
                    child = Child(CHILD_KEY_COUNTER, childMovesLeft, childMoveTable, "MIN", copy.deepcopy(parentNode.getKey()), move, coordinates, points, (copy.deepcopy(parentNode.getTotalPoints()) + points), (copy.deepcopy(parentNode.getDepth()) + 1))
                    listOfChildren.append(child)
                if parentNode.getType() == "MIN":  # if this is a min node, make max nodes
                    childMoveTable[coordinates[0]][coordinates[1]] = 1 # updates MOVE_TABLE for child - used for scoring.
                    child = Child(CHILD_KEY_COUNTER, childMovesLeft, childMoveTable, "MAX", parentNode.getKey(), move, coordinates, points, (copy.deepcopy(parentNode.getTotalPoints()) - points), (copy.deepcopy(parentNode.getDepth()) + 1))
                    listOfChildren.append(child)
                CHILD_KEY_COUNTER += 1
    return listOfChildren # list of children for parent node

def minimax(node, alpha, beta):
    global CHOSEN_DEPTH
    if node.getDepth() == ((2 * CHOSEN_DEPTH) - 1) or len(node.getMovesLeft()) == 0: # checks if node is at terminal depth or if there are more moves available after.
        return [node.getMove(), node.getTotalPoints()] # returns f(n) of terminal node with corresponding move
    if node.getType() == "MAX": # if max node
        listofChildren = generateChildren(node) # generates children board states
        maxValue = -999999 # set smallest possible value of node
        maxMove = 0 # initializes move key
        for child in listofChildren:
            valueNode = minimax(child, alpha, beta) # recursive for going down before comparing to rest of same depth nodes.
            if valueNode[1] > maxValue: # updates to highest value of children
                maxMove = child.getMove() # updates move to max value node
                maxValue = valueNode[1] # updates max value of max child
                node.setTotalPoints(child.getTotalPoints()) # passes max value up to parent.
            alpha = max(alpha, valueNode[1]) # alpha beta pruning
            if alpha >= beta:
                break # cuts off leaf nodes below
        return [maxMove, maxValue] # returns max value move and its value.
    # same thing for this chuck as above. just instead of max its min.
    if node.getType() == "MIN":
        listofChildren = generateChildren(node)
        minValue = 999999
        minMove = 0
        for child in listofChildren:
            valueNode = minimax(child, alpha, beta)
            if valueNode[1] < minValue:
                maxMove = child.getMove()
                minValue = valueNode[1]
                node.setTotalPoints(child.getTotalPoints())
            beta = min(beta, valueNode[1])
            if alpha >= beta:
                break
        return [minMove, minValue]



###################################################################
#------------------ USER INTERFACE STUFF STARTS HERE -------------------#
###################################################################


print("Welcome to Assignment 2!\n")


BoardSize = input("What Size Board Do You Want To Use?\n")
size = int(BoardSize)
print("\n\nGENERATED GAMEBOARD:")
print("-" * size * 15)
createBoard(size)
print("\n")
chosenDepth = input("How many plys do you wish the computer to calculate?\n")
CHOSEN_DEPTH = int(chosenDepth)


while (len(MOVES_LEFT) > 0):
    CHILD_KEY_COUNTER = 1
    print("\n")
    printGameBoard()
    print("-" * size * 15)
    print("PLAYER SCORE: ", USER_SCORE, "\nCOMPUTER SCORE: ", COMP_SCORE)
    print("")
    print("MOVES PLAYED - ", PLAYED_MOVES)
    print("")
    userInput = 0
    while True:
        userInput = int(input("What move do you want to play?\n"))
        if userInput in MOVES_LEFT:
            break
    userPoints = numberOfSides(userInput, MOVE_TABLE)
    addMove(userInput)
    USER_SCORE += userPoints
    PLAYED_MOVES.append(userInput)
    if (len(MOVES_LEFT) == 0):
        printGameBoard()
        break
    else:
        print("Calculating Computer Move....\n")
        node = Child(0, MOVES_LEFT, MOVE_TABLE, "MAX", 0, 0, [], 0, 0, 0)
        results = minimax(node, -999999, 999999)
        if results[0] not in MOVES_LEFT:
            results[0] = random.choice(MOVES_LEFT)
        pointsScored = numberOfSides(results[0], MOVE_TABLE)
        print("\nThe Computer played nubmer {}, and scored {} points".format(results[0], pointsScored))
        addMove(results[0])
        COMP_SCORE += pointsScored
        PLAYED_MOVES.append(results[0])
    if len(MOVES_LEFT) == 0:
        break
print("")
print("")
printGameBoard()
if COMP_SCORE > USER_SCORE:
    print("I'M SORRY YOU LOST TO THE COMPUTER!\n\nThe final score was")
    print("PLAYER SCORE: ", USER_SCORE, "\nCOMPUTER SCORE: ", COMP_SCORE)
else:
    print("CONGRATS YOU BEAT THE COMPUTER!\n\nThe final score was")
    print("PLAYER SCORE: ", USER_SCORE, "\nCOMPUTER SCORE: ", COMP_SCORE)

