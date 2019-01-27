# ASSIGNMENT 1 FOR CSC 480 - BY JACOB MIKRUT

# LOCK FOR SYNCHRONIZING THREADS FOR KEYCOUNTER (don't think i need this, but just wanted to make sure).
import threading
import time
threadLock = threading.Lock()

# iterates to add key for nodes
KEY_COUNTER = 1

GOAL = [1, 2, 3, 8, 0, 4, 7, 6, 5]
##################################
# INITIAL STATES
EASY = [1, 3, 4, 8, 6, 2, 7, 0, 5]
MEDIUM = [2, 8, 1, 0, 4, 3, 7, 6, 5]
HARD = [5, 6, 7, 4, 0, 8, 3, 2, 1]


# PRINTS STATE INTO SQUARE
def printChildren(child):
    print(child[0], "  ", child[1], "  ", child[2])
    print(child[3], "  ", child[4], "  ", child[5])
    print(child[6], "  ", child[7], "  ", child[8])
    print()
    print("-----------------------------------------")

# TRACEBACK FOR FINDING PATH FROM GOAL NODE
def printFinalPath(NodeList, node):
    traceBack = Stack()
    traceBack.push(node)
    totalPathCost = 0
    while node.getKey() > 1:
        parentKey = node.getParentKey()
        node = NodeList.get(parentKey)
        traceBack.push(node)
    while traceBack.size() > 0:
        node = traceBack.pop()
        totalPathCost = totalPathCost + node.getCost()
        print("-----------------------------------------")
        print()
        print("Node Key:", node.getKey())
        print("Node State:", node.getState())
        print("Action:", node.getAction())
        print("Depth:", node.getDepth())
        print("Edge Cost:", node.getCost())
        print("Total Cost:", totalPathCost)
        print("Heuristic Cost:", node.getHcost())
        print("f(n):", node.getHcost() + totalPathCost)
        print()
        printChildren(node.getState())

# CLASS FOR NODES IN GRAPH
class Node:
    key = 0
    state = []
    children = []
    childrenKeys = []
    visited = False
    parentKey = 0
    parentState = []
    action = ""
    depth = 0
    cost = 0
    totalPathCost = 0
    h_Cost = 0

# CONSTRUCTOR
    def __init__(self, givenKey, givenState, givenParentKey, givenParentState, givenAction, givenChildKeys, givenDepth,
                 givenCost):
        self.key = givenKey
        self.state = givenState
        self.parentKey = givenParentKey
        self.parentState = givenParentState
        self.childrenKeys = givenChildKeys
        self.action = givenAction
        self.depth = givenDepth
        self.cost = givenCost
        self.totalPathCost = givenCost

# SETTERS AND GETTERS
    def addChildren(self, givenChildren):
        self.children = givenChildren

    def addChildKeys(self, key):
        self.childrenKeys.append(key)

    def getChildKeys(self):
        return self.childrenKeys

    def setVisited(self):
        self.visited = True

    def getChildren(self):
        return self.children

    def getVisited(self):
        return self.visited

    def getState(self):
        return self.state

    def getKey(self):
        return self.key

    def getParentKey(self):
        return self.parentKey

    def getCost(self):
        return self.cost

    def getTotalPathCost(self):
        return self.totalPathCost

    def addTotalCost(self, x, y):
        self.totalPathCost = x + y

    def getParentState(self):
        return self.parentState

    def getAction(self):
        return self.action

    def setDepth(self, givenDepth):
        self.depth = givenDepth

    def getDepth(self):
        return self.depth

    def getHcost(self):
        return self.h_Cost

    def setHcost(self, cost):
        self.h_Cost = cost


# ---------  HEURSTIC FUNCTIONS --------- #

    # COUNTS NUMBER OF TILES OUT OF PLACE
    def h1(self):
        h = 0
        state = list(self.getState())
        if state[0] != 1:
            h += 1
        if state[1] != 2:
            h += 1
        if state[2] != 3:
            h += 1
        if state[3] != 8:
            h += 1
        if state[4] != 0:
            h += 1
        if state[5] != 4:
            h += 1
        if state[6] != 7:
            h += 1
        if state[7] != 6:
            h += 1
        if state[8] != 5:
            h += 1
        return h

# COUNTS NUMBER OF POSITIONS EACH TILE IS FROM CORRECT POSITION
    def h2(self):
        total = 0
        for x in self.getState():
            pos1 = self.getState().index(x)
            pos2 = GOAL.index(x)
            h = abs(pos1 - pos2)
            total = total + h
        return total

# COUNTS NUMBER OF POSITIONS EACH TILE IS FROM CORRECT POSITION AND MULTIPLIES IT WITH THEIR VALUE/COST
    def h3(self):
        total = 0
        for x in self.getState():
            pos1 = self.getState().index(x)
            pos2 = GOAL.index(x)
            h = abs(pos1 - pos2)
            total = (total + (h * x))
        return total

    # SUCCESSOR METHOD FOR SUCCESSIVE CHILD STATES OF CURRENT STATE
    def generateChildren(self):
        # DEPENDING ON THE CURRENT STATE, THERE ARE UP TO 4 POTENTIAL MOVES/CHILDREN
        # CREATING COPIES OF ORIGINAL STATE BECAUSE I DON'T KNOW HOW MANY CHILDREN OR WHICH ONE EQUALS PARENT STATE
        child1 = list(self.state)
        child2 = list(self.state)
        child3 = list(self.state)
        child4 = list(self.state)
        action1 = ""
        action2 = ""
        action3 = ""
        action4 = ""
        cost1 = 0
        cost2 = 0
        cost3 = 0
        cost4 = 0
        tempChildList = []
        # MOVE SET DEPENDING ON WHICH INDEX 0 IS LOCATED.
        if self.state[0] == 0:
            cost1 = self.state[1]
            child1[0] = child1[1]
            child1[1] = 0
            action1 = "Right"
            cost2 = self.state[3]
            child2[0] = child2[3]
            child2[3] = 0
            action2 = "Down"
        elif self.state[1] == 0:
            cost1 = self.state[0]
            child1[1] = child1[0]
            child1[0] = 0
            action1 = "Left"
            cost2 = self.state[2]
            child2[1] = child2[2]
            child2[2] = 0
            action2 = "Right"
            cost3 = self.state[4]
            child3[1] = child3[4]
            child3[4] = 0
            action3 = "Down"
        elif self.state[2] == 0:
            cost1 = self.state[1]
            child1[2] = child1[1]
            child1[1] = 0
            action1 = "Left"
            cost2 = self.state[5]
            child2[2] = child2[5]
            child2[5] = 0
            action2 = "Down"
        elif self.state[3] == 0:
            cost1 = self.state[0]
            child1[3] = child1[0]
            child1[0] = 0
            action1 = "Up"
            cost2 = self.state[4]
            child2[3] = child2[4]
            child2[4] = 0
            action2 = "Right"
            cost3 = self.state[6]
            child3[3] = child3[6]
            child3[6] = 0
            action3 = "Down"
        elif self.state[4] == 0:
            cost1 = self.state[1]
            child1[4] = child1[1]
            child1[1] = 0
            action1 = "Up"
            cost2 = self.state[3]
            child2[4] = child2[3]
            child2[3] = 0
            action2 = "Left"
            cost3 = self.state[5]
            child3[4] = child3[5]
            child3[5] = 0
            action3 = "Right"
            cost4 = self.state[7]
            child4[4] = child4[7]
            child4[7] = 0
            action4 = "Down"
        elif self.state[5] == 0:
            cost1 = self.state[2]
            child1[5] = child1[2]
            child1[2] = 0
            action1 = "Up"
            cost2 = self.state[4]
            child2[5] = child2[4]
            child2[4] = 0
            action2 = "Left"
            cost3 = self.state[8]
            child3[5] = child3[8]
            child3[8] = 0
            action3 = "Down"
        elif self.state[6] == 0:
            cost1 = self.state[3]
            child1[6] = child1[3]
            child1[3] = 0
            action1 = "Up"
            cost2 = self.state[7]
            child2[6] = child2[7]
            child2[7] = 0
            action2 = "Right"
        elif self.state[7] == 0:
            cost1 = self.state[4]
            child1[7] = child1[4]
            child1[4] = 0
            action1 = "Up"
            cost2 = self.state[6]
            child2[7] = child2[6]
            child2[6] = 0
            action2 = "Right"
            cost3 = self.state[8]
            child3[7] = child3[8]
            child3[8] = 0
            action3 = "Left"
        elif self.state[8] == 0:
            cost1 = self.state[5]
            child1[8] = child1[5]
            child1[5] = 0
            action1 = "Up"
            cost2 = self.state[7]
            child2[8] = child2[7]
            child2[7] = 0
            action2 = "Left"
        # CHECKS STATE OF 4 POTENTIAL MOVES TO SEE IF THEY HAVE CHANGED FROM ORIGINAL STATE AND
        # IF STATE IS EQUAL TO PARENT STATE. IF NOT EQUAL TO ORIGINAL STATE OR PARENT STATE
        # THE CHILD STATE IS PLACED INTO A TEMP CHILD LIST OF NODES THATS RETURNED TO SEARCH ALGO.
        parentDepth = self.getDepth()
        if child1 not in [self.state, self.parentState]:
            # LOCKS THREADS SO GLOBAL KEY_COUNTER DOESN'T MESS UP.
            with threadLock:
                global KEY_COUNTER
                KEY_COUNTER += 1
            childNode1 = Node(KEY_COUNTER, child1, self.key, self.state, action1, [], parentDepth + 1, cost1)
            tempChildList.append(childNode1)
        if child2 not in [self.state, self.parentState]:
            with threadLock:
                KEY_COUNTER += 1
            childNode2 = Node(KEY_COUNTER, child2, self.key, self.state, action2, [], parentDepth + 1, cost2)
            tempChildList.append(childNode2)
        if child3 not in [self.state, self.parentState]:
            with threadLock:
                KEY_COUNTER += 1
            childNode3 = Node(KEY_COUNTER, child3, self.key, self.state, action3, [], parentDepth + 1, cost3)
            tempChildList.append(childNode3)
        if child4 not in [self.state, self.parentState]:
            with threadLock:
                KEY_COUNTER += 1
            childNode4 = Node(KEY_COUNTER, child4, self.key, self.state, action4, [], parentDepth + 1, cost4)
            tempChildList.append(childNode4)
        # RETURNS LIST OF CHILD NODES
        return tempChildList


def sortQueue(q):
    # q = list of lists
    # selection sort for multidimensinonal list
    for i in range(len(q)):
        minimum = i
        for j in range(i + 1, len(q)):
            # select smallest h1 value in tuple.
            if q[j][0] < q[minimum][0]:
                minimum = j
        # put it at the front
        q[minimum], q[i] = q[i], q[minimum]
    return q

# QUEUE CLASS FOR FIFO UTILITIES
class Queue:
    def __init__(self):
        self.queue = list()

    # add item to Queue
    def push(self, data):
        self.queue.insert(0, data)

    # returns item from Queue
    def pop(self):
        if len(self.queue) > 0:
            return self.queue.pop()

    # checks size of queue
    def size(self):
        return len(self.queue)

    # prints size of queue
    def printQueue(self):
        return self.queue

 # STACK DATA STRUCTURE CLASS FOR LIFO UTILITIES
class Stack:
    def __init__(self):
        self.items = []

    # checks if stack is empty
    def isEmpty(self):
        return self.items == []

    # adds item to stack
    def push(self, item):
        self.items.append(item)

    # returns item
    def pop(self):
        return self.items.pop()

    # returns size of stack
    def size(self):
        return len(self.items)

    def emptyStack(self):
        self.items.clear()


# DICTIONARY CLASS SAVING ALL SEARCHED NODES
class Graph:
    def __init__(self):
        self.dict = {}

    def add(self, key, value):
        self.dict.update({key: value})

    def get(self, key):
        return self.dict.get(key)

    def print(self):
        print(self.dict.items())

    def emptyGraph(self):
        self.dict.clear()

    def size(self):
        return len(self.dict)

# FOR USE WITH A*.
# CHECKS IF STATE HAS BEEN OBSERVED THEN COMPARES THEIR F(N) VALUE.
def checkReplaceVisitedNodes(nodeList, node):
    for element in nodeList:
        if element.getState() == node.getState():
            if (element.getHcost() + element.getTotalPathCost()) > (node.getHcost() + node.getTotalPathCost()):
                loc = nodeList.index(element)
                nodeList[loc] = node
            return nodeList
    return nodeList

# FOR USE WITH A*.
# DOES SAME AS ABOVE, JUST DOESN'T REPLACE ONLY RETURNS A BOOLEAN
def checkVisitedNodes(nodeList, node):
    for element in nodeList:
        if element.getState() == node.getState():
            if (element.getHcost() + element.getTotalPathCost()) > (node.getHcost() + node.getTotalPathCost()):
                return True
    return False

# FOR UNIFORM COST SEARCH
# CHECKS IF STATE HAS BEEN OBSERVED THEN COMPARES THE TOTAL PATH COST
def replaceNodeCost(nodeList, node):
    for element in nodeList:
        if element.getState() == node.getState():
            if (element.getHcost() + element.getTotalPathCost()) > (node.getHcost() + node.getTotalPathCost()):
                loc = nodeList.index(element)
                nodeList[loc] = node
            return nodeList
    return nodeList

def checkNodeCost(nodeList, node):
    for element in nodeList:
        if element.getState() == node.getState():
            if (element.getHcost() + element.getTotalPathCost()) > (node.getHcost() + node.getTotalPathCost()):
                return True
    return False


##### -------------------------------------------
##### SEARCH ALGORITHMS
##### -------------------------------------------

# ----------- BREADTH-FIRST SEARCH ------------- #

# THESE COMMENTS ARE FOR ME.
def bfs(startNode):
    start = time.time()
    searchQueue = Queue() # FIFO queue that hold nodes that should be searched next
    NodeList = Graph()  # dictionary for all searched nodes { STATE.KEY : NODE }
    checkedStates = []  # state checking to reduce redundancy.

    # adding initial node to queue
    searchQueue.push(startNode)

    # observing current node state
    while searchQueue.size() > 0:
        node = searchQueue.pop()
        print("Key:", node.getKey(), " :  State:", node.getState(), ":  Depth:", node.getDepth(), ":  Queue Size:", searchQueue.size())

        # adds node to check states and to node list
        checkedStates.append(node.getState())
        NodeList.add(node.getKey(), node)

        # if node is a goal state
        if node.getState() == GOAL:
            print("you've solved the puzzle")

            # prints solution path
            printFinalPath(NodeList, node)

            # prints and calculates total runtime.
            end = time.time()
            print("\nTotal Runtime:", end - start, "seconds")
            print("Total Nodes visited:", NodeList.size(), "\n")
            return

        # loop for adding child states to the queue
        else:
            node.setVisited()
            children = node.generateChildren()
            for element in children:
            # for each child created, checks if we've seen state before
            # if state hasn't been seen, added to search queue
                if element.getState() not in checkedStates:
                    searchQueue.push(element)

# ----------- DEPTH-FIRST SEARCH ------------- #

def dfs(startNode):
    start = time.time()
    s = Stack()
    visitedStates = []
    NodeList = Graph()
    s.push(startNode)

    while s.size() > 0:

        # pops element LIFO
        node = s.pop()
        if node.getState() in visitedStates:
            continue
        NodeList.add(node.getKey(), node)
        print("Key:", node.getKey(), " :  State:", node.getState(), ":  Depth:", node.getDepth(), ":  Stack Size:", s.size())

        # found goal state
        if node.getState() == GOAL:
            print("you have solved the puzzle")

            # prints solution path
            printFinalPath(NodeList, node)

            # calculates runtime
            end = time.time()
            print("\nTotal Runtime:", end - start, "seconds")
            print("Total Nodes visited:", NodeList.size(), "\n")
            return
        # loop for adding child nodes to stack
        if node.getVisited() == False:
            # if unseen state
            if node.getState() not in visitedStates:
                visitedStates.append(node.getState())
                node.setVisited()

                # generate children with successor funtion
                children = node.generateChildren()
                node.addChildren(children)
                # reversed children list because i was traversing the wrong side of the tree, so this hurried up the solution
                for child in reversed(children):
                    key = child.getKey()
                    # over complicated because i had an error and this was how i caught it.
                    if key not in node.getChildKeys():
                        node.addChildKeys(key)
                        s.push(child)

# ----------- ITERATIVE DEEPENING ------------- #

def IterativeDeepening(startNode):
    start = time.time()
    currentDepth = 0
    maxDepth = 1  #  sets the max dep search is allowed to search. dfs with depth limit
    s = Stack()
    NodeList = Graph()
    while currentDepth < 1000:
        maxDepth = maxDepth + 1
        NodeList.emptyGraph()
        s.emptyStack()
        s.push(startNode)

        while currentDepth <= maxDepth:
            if s.size() > 0:
                node = s.pop()
            else:
                break
            print("Key:", node.getKey(), " :  State:", node.getState(), ":  Depth:", node.getDepth(), ":  Stack Size:", s.size())
            NodeList.add(node.getKey(), node)

            # found goal node
            if node.getState() == GOAL:
                print("you have solved the puzzle")

                # prints solution path
                printFinalPath(NodeList, node)

                # calculates and prints total run time.
                end = time.time()
                print("\nTotal Runtime:", end - start, "seconds")
                print("Total Nodes visited:", NodeList.size(), "\n")
                return

            # meat and potatoes
            if node.getVisited() == True:
                continue
            NodeList.add(node.getKey(), node)
            # make sure to only add children within depth limit
            if node.getDepth() < maxDepth:
                # should be same as dfs from here
                children = node.generateChildren()
                node.addChildren(children)
                for child in children:
                    if child.getState() != node.getState():
                        # extra check here for checking duplicating states. redundant.
                        if child.getState() != node.getParentState():
                            key = child.getKey()
                            if key not in node.getChildKeys():
                                node.addChildKeys(key)
                                s.push(child)

# ----------- UNIFORM COST SEARCH ------------- #
# Last three algos are the same except, UC uses path weight as cost, best uses only the Heuristic, and A* uses both.
def UniformCost(startNode):
    start = time.time()
    NodeList = Graph()
    visitedStates = []
    visitedStatesWithCost = []
    costList = []
    costList.append([startNode.getTotalPathCost(), startNode])

    while len(costList) > 0:
        sortQueue(costList)
        min = costList.pop(0)
        node = min[1]
        NodeList.add(node.getKey(), node)
        print("Key:", node.getKey(), " :  State:", node.getState(), ":  Cost:", node.getTotalPathCost(), ":  Queue Size:", len(costList))

        # found goal state
        if node.getState() == GOAL:
            print("you found the goal!!")
            # print solution path
            printFinalPath(NodeList, node)
            # calculates and prints runtime
            end = time.time()
            print("\nTotal Runtime:", end - start, "seconds")
            print("Total Nodes visited:", NodeList.size())
            print("Size of Queue:", )
            return
        # expand node
        children = node.generateChildren()
        # once expanded, add node to visited list
        if node.getState() not in visitedStates:
            visitedStates.append(node.getState())
            visitedStatesWithCost.append([node.getTotalPathCost(), node.getState()])
        else:
            # compares total cost of current node and previous node of same state
            for element in visitedStatesWithCost:
                if node.getState() == element[1]:
                    if node.getTotalPathCost() < element[0]:
                        loc = visitedStatesWithCost.index(element)
                        visitedStatesWithCost[loc] = [node.getTotalPathCost(), node.getState()]
        # add cost to total path cost for node
        for child in children:
            child.addTotalCost(child.getCost(), node.getTotalPathCost())
            # simple add state and cost to to queue if haven't been seen before
            if child.getState() not in visitedStates:
                costList.append([child.getTotalPathCost(), child])
            else:
                # compares total costs of states before adding child on queue
                for element in visitedStatesWithCost:
                    if child.getState() == element[1]:
                        if child.getTotalPathCost() < element[0]:
                            costList.append([child.getTotalPathCost(), child])

# ----------- (GREEDY) BEST-FIRST SEARCH ------------- #

def Best(startNode):
    start = time.time()
    NodeList = Graph()
    bestFirst = []
    visitedStates = []
    hCostList = []
    bestFirst.append([startNode.h1(), startNode])
    while len(bestFirst) > 0:
        sortQueue(bestFirst)
        min_h1 = bestFirst.pop(0)
        node = min_h1[1]
        print("Key:", node.getKey(), " :  State:", node.getState(), ":  Depth:", node.getDepth(), ":  Queue Size:", len(bestFirst))
        NodeList.add(node.getKey(), node)

        # FOUND GOAL NODE
        if node.h1() == 0:
            print("\nyou solved the puzzle!!\n")

            # PRINTS SOLUTION PATH
            printFinalPath(NodeList, node)

            # CALCULATES AND PRINTS TOTAL RUNTIME.
            end = time.time()
            print("\nTotal Runtime:", end - start, "seconds")
            print("Total Nodes visited:", NodeList.size(), "\n")
            return
        if node.getState() not in visitedStates:
            visitedStates.append(node.getState())
            hCostList.append([node.h1(), node.getState()])
        else:
            for element in hCostList:
                if node.getState() == element[1]:
                    if node.h1() < element[0]:
                        loc = hCostList.index(element)
                        hCostList[loc] = [node.getTotalPathCost(), node.getState()]
        children = node.generateChildren()
        for child in children:
            if child.getState() not in visitedStates:
                element = [child.h1(), child]
                bestFirst.append(element)
            else:
                # compares total costs of states before adding child on queue
                for element in hCostList:
                    if child.getState() == element[1]:
                        if child.getTotalPathCost() < element[0]:
                            bestFirst.append([child.h1(), child])

# ----------- A* SEARCH ------------- #

def A_STAR(startNode, h):
    start = time.time()  #start calculating execution time
    NodeList = Graph()  # {node.getKey() : node}
    pathScores = []  # [ [A* score, node] ] - sorted by A* score
    visitedNodes = []  # [node.getState()] - used to compare f(n) of nodes with same state
    visitedStates = []  # [node.getState()] - allows for quicker checking to see if node has been seen or not

    # depending on which heuristic you pick in user interface
    if h == 1:
        ascore = startNode.getTotalPathCost() + startNode.h1()
    if h == 2:
        ascore = startNode.getTotalPathCost() + startNode.h2()
    if h == 3:
        ascore = startNode.getTotalPathCost() + startNode.h3()
    pathScores.append([ascore, startNode])  # f(n) =

    while len(pathScores) > 0:
        sortQueue(pathScores)
        min = pathScores.pop(0)
        node = min[1]
        NodeList.add(node.getKey(), node)
        print("Key:", node.getKey(), " :  State:", node.getState(), ":  Depth:", node.getDepth(), ":  Queue Size:", len(pathScores))

        # FOUND GOAL NODE
        if node.getState() == GOAL:
            print("\nyou solved the puzzle!!\n")
            # prints solution path
            printFinalPath(NodeList, node)
            # calculates and prints runtime
            end = time.time()
            print("\nTotal Runtime:", end - start, "seconds")
            print("Total Nodes visited:", NodeList.size(), "\n")
            return

        # checks if state is in visited states and replaces if f(n) is lower
        visitedNodes = checkReplaceVisitedNodes(visitedNodes, node)
        visitedStates.append(node.getState())
        children = node.generateChildren()
        # changes with flag inputed via user interface
        for child in children:
            if h == 1:
                h_cost = child.h1()
            if h == 2:
                h_cost = child.h2()
            if h == 3:
                h_cost = child.h3()
            child.setHcost(h_cost)
            if child.getState() not in visitedStates:
                child.addTotalCost(child.getCost(), node.getTotalPathCost())
                pathScores.append([child.getTotalPathCost() + h_cost, child])
            else:
                if checkVisitedNodes(visitedNodes, child):
                    child.addTotalCost(child.getCost())
                    pathScores.append([child.getTotalPathCost() + h_cost, child])

##### -------------------------------------------
##### USER INTERFACE CODE
##### -------------------------------------------

while True:
    difficulty = input("Choose a difficulty (Enter the corresponding number):\n1). EASY\n2). MEDIUM\n3). HARD\n")
    if difficulty == "1":
        startNode = Node(1, EASY, 0, [], "Start", [], 1, 0)
        break
    if difficulty == "2":
        startNode = Node(1, MEDIUM, 0, [], "Start", [], 1, 0)
        break
    if difficulty == "3":
        startNode = Node(1, HARD, 0, [], "Start", [], 1, 0)
        break

while True:
    userInput = input("What search algorithm do you wish to run?\n1). BREATH-FIRST SEARCH\n2). DEPTH-FIRST SEARCH\n3). ITERATIVE DEEPENING\n4). UNIFORM COST SEARCH\n5). (GREEDY) BEST-FIRST SEARCH\n6). A* SEARCH\n")
    if userInput == "1":
        bfs(startNode)
        break
    if userInput == "2":
        dfs(startNode)
        break
    if userInput == "3":
        IterativeDeepening(startNode)
        break
    if userInput == "4":
        UniformCost(startNode)
        break
    if userInput == "5":
        Best(startNode)
        break
    if userInput == "6":
        while True:
            hValue = input("Which Heuristic do you want to run with A* Search?\n1). HEURISTIC #1 \n2). HEURISTIC #2\n3). HEURISTIC #3\n")
            if hValue == "1":
                A_STAR(startNode, 1)
                break
            if hValue == "2":
                A_STAR(startNode, 2)
                break
            if hValue == "3":
                A_STAR(startNode, 3)
                break
    if hValue in ["1", "2", "3"]:
        break


