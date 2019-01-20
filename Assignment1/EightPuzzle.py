# ASSIGNMENT 1 FOR CSC 480 - BY JACOB MIKRUT

GOAL = [1, 2, 3, 8, 0, 4, 7, 6, 5]
##################################
##################################
# INITIAL STATES
EASY = [1, 3, 4, 8, 6, 2, 7, 0, 5]
MEDIUM = [2, 8, 1, 0, 4, 3, 7, 6, 5]
HARD = [5, 6, 7, 4, 0, 8, 3, 2, 1]


def printChildren(child):
    print(child[0], "   ", child[1], "   ", child[2])
    print(child[3], "   ", child[4], "   ", child[5])
    print(child[6], "   ", child[7], "   ", child[8])
    print("-----------------------------------------")



class Node:
    key = 0
    state = []
    children = []
    visited = False
    parentKey = 0
    parentState = []
    action = ""
    depth = 0
    cost = 0

    def __init__(self, givenKey, givenState, givenParentKey, givenParentState, givenAction, givenDepth, givenCost):
        self.key = givenKey
        self.state = givenState
        self.parentKey = givenParentKey
        self.parentState = givenParentState
        self.action = givenAction
        self.depth = givenDepth
        self.cost = givenCost

    def addChild(self, givenChild):
        if givenChild != self.parentState:
            self.children.append(givenChild)

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

    def generateChildren(self):
        #self.myLock = threading.lock()
        child1 = list(self.state)
        child2 = list(self.state)
        child3 = list(self.state)
        child4 = list(self.state)
        action1 = ""
        action2 = ""
        action3 = ""
        action4 = ""
        tempChildList = []
        if self.state[0] == 0:
            child1[0] = child1[1]
            child1[1] = 0
            action1 = "Right"
            child2[0] = child2[3]
            child2[3] = 0
            action2 = "Down"
        elif self.state[1] == 0:
            child1[1] = child1[0]
            child1[0] = 0
            action1 = "Left"
            child2[1] = child2[2]
            child2[2] = 0
            action2 = "Down"
            child3[1] = child3[4]
            child3[4] = 0
            action3 = "Right"
        elif self.state[2] == 0:
            child1[2] = child1[1]
            child1[1] = 0
            action1 = "Left"
            child2[2] = child2[5]
            child2[5] = 0
            action2 = "Down"
        elif self.state[3] == 0:
            child1[3] = child1[0]
            child1[0] = 0
            action1 = "Up"
            child2[3] = child2[4]
            child2[4] = 0
            action2 = "Right"
            child3[0] = child3[6]
            child3[6] = 0
            action3 = "Down"
        elif self.state[4] == 0:
            child1[4] = child1[1]
            child1[1] = 0
            action1 = "Up"
            child2[4] = child2[3]
            child2[3] = 0
            action2 = "Left"
            child3[4] = child3[5]
            child3[5] = 0
            action3 = "Right"
            child4[4] = child4[7]
            child4[7] = 0
            action4 = "Down"
        elif self.state[5] == 0:
            child1[5] = child1[2]
            child1[2] = 0
            action1 = "Up"
            child2[5] = child2[4]
            child2[4] = 0
            action2 = "Left"
            child3[5] = child3[8]
            child3[8] = 0
            action3 = "Down"
        elif self.state[6] == 0:
            child1[6] = child1[3]
            child1[3] = 0
            action1 = "Up"
            child2[6] = child2[7]
            child2[7] = 0
            action2 = "Right"
        elif self.state[7] == 0:
            child1[7] = child1[4]
            child1[4] = 0
            action1 = "Up"
            child2[7] = child2[6]
            child2[6] = 0
            action2 = "Right"
            child3[7] = child3[8]
            child3[8] = 0
            action3 = "Left"
        elif self.state[8] == 0:
            child1[8] = child1[5]
            child1[5] = 0
            action1 = "Up"
            child2[8] = child2[7]
            child2[7] = 0
            action2 = "Left"
        keyCounter = self.key
        if child1 not in [self.state, self.parentState]:
            # new child1
            # givenKey, givenState, givenParentKey, givenParentState, givenAction, givenDepth, givenCost
            keyCounter += 1
            childNode1 = Node(keyCounter, child1, self.key, self.state, action1, self.depth + 1, 0)
            tempChildList.append(childNode1)
        if child2 not in [self.state, self.parentState]:
            keyCounter += 1
            childNode2 = Node(keyCounter, child2, self.key, self.state, action2, self.depth + 1, 0)
            tempChildList.append(childNode2)
        if child3 not in [self.state, self.parentState]:
            keyCounter += 1
            childNode3 = Node(keyCounter, child1, self.key, self.state, action3, self.depth + 1, 0)
            tempChildList.append(childNode3)
        if child4 not in [self.state, self.parentState]:
            keyCounter += 1
            childNode4 = Node(keyCounter, child1, self.key, self.state, action4, self.depth + 1, 0)
            tempChildList.append(childNode4)
        return tempChildList


# Queue Class
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


class Graph:
    def __init__(self):
        self.dict = {}

    def add(self, key, value):
        self.dict.update({key: value})

    def get(self, key):
        self.dict.get(key)

    def print(self):
        self.dict.items()


def bfs(startNode):
    # print(startNode.state)
    # print(startNode.action)
    currentDepth = Queue()
    foundPath = Queue()
    NodeList = Graph()
    checkedStates = []

    currentDepth.push(startNode)

    # check if state is goal
    print(startNode.state)
    while currentDepth.size() > 0:
        node = currentDepth.pop()
        print(node.getKey())
        checkedStates.append(node.getState())
        NodeList.add(node.getKey(), node)
        if node.getVisited() == False:
            if node.getState() != GOAL:
                node.setVisited()
                children = node.generateChildren()
                for element in children:
                    if element.getState not in checkedStates:
                        currentDepth.push(element)

            else:
                print("you've solved the puzzle")
                foundPath.push(node)
                
                break
    # print("DOING BFS RIGHT NOW PLEASE WAIT")


while True:
    userInput = input("what Program do you want to run?")
    if userInput == "yes":
        #  givenKey, givenState, givenParentKey, givenParentState, givenAction, givenDepth, givenCost
        startNode = Node(1, EASY, 0, [], "Start", 1, 0)
        bfs(startNode)
