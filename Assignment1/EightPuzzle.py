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
    visited = bool
    parent = []
    action = ""
    depth = 0
    cost = 0

    def __init__(self, givenKey, givenState, givenParent, givenAction, givenDepth, givenCost):
        self.key = givenKey
        self.state = givenState
        self.parent = givenParent
        self.action = givenAction
        self.depth = givenDepth
        self.cost = givenCost

    def addChild(self, givenChild):
        if givenChild != self.parent:
            self.children.append(givenChild)

    def visitedChild(self):
        self.visited = True

    def getChildren(self):
        return self.children

    def generateChildren(self):
        child1 = list(self.state)
        child2 = list(self.state)
        child3 = list(self.state)
        child4 = list(self.state)
        if self.state[0] == 0:
            # first child
            child1[0] = child1[1]
            child1[1] = 0
            # first 
            child2[0] = child2[3]
            child2[3] = 0

        elif self.state[1] == 0:
            child1 = list(self.state)
            child1[1] = child1[0]
            child1[0] = 0
            child2 = list(self.state)
            child2[1] = child2[2]
            child2[2] = 0
            child3 = list(self.state)
            child3[1] = child3[4]
            child3[4] = 0
        elif self.state[2] == 0:
            child1 = list(self.state)
            child1[2] = child1[1]
            child1[1] = 0
            child2 = list(self.state)
            child2[2] = child2[5]
            child2[5] = 0
        elif self.state[3] == 0:
            child1 = list(self.state)
            child1[3] = child1[0]
            child1[0] = 0
            child2 = list(self.state)
            child2[3] = child2[4]
            child2[4] = 0
            child3 = list(self.state)
            child3[0] = child3[6]
            child3[6] = 0
        elif self.state[4] == 0:
            child1 = list(self.state)
            child1[4] = child1[1]
            child1[1] = 0
            child2 = list(self.state)
            child2[4] = child2[3]
            child2[3] = 0
            child3 = list(self.state)
            child3[4] = child3[5]
            child3[5] = 0
            child4 = list(self.state)
            child4[4] = child4[7]
            child4[7] = 0
        elif self.state[5] == 0:
            child1 = list(self.state)
            child1[5] = child1[2]
            child1[2] = 0
            child2 = list(self.state)
            child2[5] = child2[4]
            child2[4] = 0
            child3 = list(self.state)
            child3[5] = child3[8]
            child3[8] = 0
        elif self.state[6] == 0:
            child1 = list(self.state)
            child1[6] = child1[3]
            child1[3] = 0
            child2 = list(self.state)
            child2[6] = child2[7]
            child2[7] = 0
        elif self.state[7] == 0:
            child1 = list(self.state)
            child1[7] = child1[4]
            child1[4] = 0
            child2 = list(self.state)
            child2[7] = child2[6]
            child2[6] = 0
            child3 = list(self.state)
            child3[7] = child3[8]
            child3[8] = 0
            # check for if parent is present an if so, remove matching move.
            print(child1)
            print(child2)
            print(child3)
            # print(self.state)
            printChildren(child1)
            printChildren(child2)
            printChildren(child3)
        elif self.state[8] == 0:
            child1 = list(self.state)
            child1[8] = child1[5]
            child1[5] = 0
            child2 = list(self.state)
            child2[8] = child2[7]
            child2[7] = 0



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
    print(startNode.state)
    print(startNode.action)
    currentDepth = Queue()
    nextDepth = Queue()
    NodeList = Graph()
    checkedStates = []


    print("DOING BFS RIGHT NOW PLEASE WAIT")


while True:
    userInput = input("what Program do you want to run?")
    if userInput == "yes":
        #  givenKey, givenState, givenParent, givenAction, givenDepth, givenCost
        startNode = Node(1, EASY, [], "Start", 1, 0)
        bfs(startNode)
