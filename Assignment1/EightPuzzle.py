# ASSIGNMENT 1 FOR CSC 480 - BY JACOB MIKRUT

# LOCK FOR SYNCHRONIZING THREADS FOR KEYCOUNTER
import threading

threadLock = threading.Lock()

# iterates to add key for nodes
KEY_COUNTER = 1

GOAL = [1, 2, 3, 8, 0, 4, 7, 6, 5]
##################################
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


# CLASS FOR NODES IN GRAPH
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

    def getParentKey(self):
        return self.parentKey

    def getCost(self):
        return self.cost

    def getParentState(self):
        return self.parentState

    def getAction(self):
        return self.action

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
        tempChildList = []
        # MOVE SET DEPENDING ON WHICH INDEX 0 IS LOCATED.
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
        # CHECKS STATE OF 4 POTENTIAL MOVES TO SEE IF THEY HAVE CHANGED FROM ORIGINAL STATE AND
        # IF STATE IS EQUAL TO PARENT STATE. IF NOT EQUAL TO ORIGINAL STATE OR PARENT STATE
        # THE CHILD STATE IS PLACED INTO A TEMP CHILD LIST OF NODES THATS RETURNED TO SEARCH ALGO.
        if child1 not in [self.state, self.parentState]:
            # LOCKS THREADS SO GLOBAL KEY_COUNTER DOESN'T MESS UP.
            with threadLock:
                global KEY_COUNTER
                KEY_COUNTER += 1
            childNode1 = Node(KEY_COUNTER, child1, self.key, self.state, action1, self.depth + 1, 0)
            tempChildList.append(childNode1)
        if child2 not in [self.state, self.parentState]:
            with threadLock:
                # global keyCounter
                KEY_COUNTER += 1
            childNode2 = Node(KEY_COUNTER, child2, self.key, self.state, action2, self.depth + 1, 0)
            tempChildList.append(childNode2)
        if child3 not in [self.state, self.parentState]:
            with threadLock:
                # global keyCounter
                KEY_COUNTER += 1
            childNode3 = Node(KEY_COUNTER, child1, self.key, self.state, action3, self.depth + 1, 0)
            tempChildList.append(childNode3)
        if child4 not in [self.state, self.parentState]:
            with threadLock:
                # global keyCounter
                KEY_COUNTER += 1
            childNode4 = Node(KEY_COUNTER, child1, self.key, self.state, action4, self.depth + 1, 0)
            tempChildList.append(childNode4)
        # RETURNS LIST OF CHILD NODES
        return tempChildList


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


class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

# CUSTOM DICTIONARY CLASS SAVING ALL SEARCHED NODES
class Graph:
    def __init__(self):
        self.dict = {}

    def add(self, key, value):
        self.dict.update({key: value})

    def get(self, key):
        return self.dict.get(key)

    def print(self):
        print(self.dict.items())


def bfs(startNode):
    # FIFO QUEUE THAT HOLDS NODES THAT SHOULD BE SEARCHED NEXT
    searchQueue = Queue()
    # ONCE GOAL STATE IS FOUND, NODES ARE ADDED TO FOUND PATH QUEUE
    foundPath = Queue()
    # DICTIONARY FOR ALL SEARCHED NODES { STATE.KEY : NODE }
    NodeList = Graph()
    # STATE CHECKING TO NARROW DOWN REDUNDANCY.
    checkedStates = []
    # ALLOWS ME TO ITERATE THROUGH FOUND PATH IN REVERSE
    solvePath = []
    # BEGINS SEARCHING GRAPH/TREE WITH TOP NODE
    searchQueue.push(startNode)
    # ALLOWS TO DOUBLE CHECKING INITIAL STATE IN CASE CHANGING DIFFICULTIES.
    # print(startNode.state)
    while searchQueue.size() > 0:
        node = searchQueue.pop()
        # PRINTS KEY FOR NODE THAT IS CURRENTLY BEING SEARCHED/VISITED
        # print(node.getKey())
        # ADDS STATE TO CHECK STATES
        checkedStates.append(node.getState())
        # ADDS CURRENT NODE TO GRAPH/DICTIONARY OF ALL SEARCHED NODES
        NodeList.add(node.getKey(), node)
        # IF WE HAVEN'T SEARCHED THIS NODE / DOESN'T EQUAL GOAL STATE, WE GENERATE ITS CHILD STATES
        if node.getVisited() == False:
            # IF STATE EQUALS GOAL STATE -> CONTINUE DOWN TO ELSE BLOCK
            if node.getState() != GOAL:
                # CHANGES BOOLEAN STORED IN NODE -> VISITED = TRUE
                node.setVisited()
                # GENERATES AND RETURN LIST OF CHILD STATE NODES
                children = node.generateChildren()
                for element in children:
                    # FOR EACH CHILD CREATED, CHECKS IF WE'VE SEEN THE STATE BEFORE,
                    # IF STATE HASN'T BEEN SEARCHED BEFORE, ITS ADDED TO SEARCH QUEUE
                    if element.getState not in checkedStates:
                        searchQueue.push(element)
            # IF STATE EQUALS GOAL STATE
            else:
                # print("you've solved the puzzle")
                # print(node.getKey())
                foundPath.push(node)
                while foundPath.size() > 0:
                    print(node.getKey())
                    if node.getKey() == 1:
                        solvePath.append(1)
                        break
                    key = node.getKey()
                    solvePath.append(key)
                    parentKey = node.getParentKey()
                    # print(parentKey)
                    # NodeList.print()
                    node = NodeList.get(parentKey)
                    # print(node.getKey)
                    foundPath.pop()
                    foundPath.push(node)
                for element in reversed(solvePath):
                    print("-----------------------------------------")
                    node = NodeList.get(element)
                    print()
                    print("Node Key:", node.getKey())
                    print("Node State:", node.getState())
                    print("Action:", node.getAction())
                    print("Cost:", node.getCost())
                    print()
                    printChildren(node.getState())
                break


def dfs(startNode):
    # LIFO STACK THAT HOLDS NODES THAT SHOULD BE SEARCHED NEXT
    searchQueue = Stack()
    # ONCE GOAL STATE IS FOUND, NODES ARE ADDED TO FOUND PATH QUEUE
    foundPath = Queue()
    # DICTIONARY FOR ALL SEARCHED NODES { STATE.KEY : NODE }
    NodeList = Graph()
    # STATE CHECKING TO NARROW DOWN REDUNDANCY.
    checkedStates = []
    # ALLOWS ME TO ITERATE THROUGH FOUND PATH IN REVERSE
    solvePath = []
    # BEGINS SEARCHING GRAPH/TREE WITH TOP NODE
    searchQueue.push(startNode)
    # ALLOWS TO DOUBLE CHECKING INITIAL STATE IN CASE CHANGING DIFFICULTIES.
    # print(startNode.state)
    while searchQueue.size() > 0:
        node = searchQueue.pop()
        # PRINTS KEY FOR NODE THAT IS CURRENTLY BEING SEARCHED/VISITED
        print(node.getKey())
        # ADDS STATE TO CHECK STATES
        checkedStates.append(node.getState())
        # ADDS CURRENT NODE TO GRAPH/DICTIONARY OF ALL SEARCHED NODES
        NodeList.add(node.getKey(), node)
        # IF WE HAVEN'T SEARCHED THIS NODE / DOESN'T EQUAL GOAL STATE, WE GENERATE ITS CHILD STATES
        if node.getVisited() == False:
            # IF STATE EQUALS GOAL STATE -> CONTINUE DOWN TO ELSE BLOCK
            if node.getState() != GOAL:
                # CHANGES BOOLEAN STORED IN NODE -> VISITED = TRUE
                node.setVisited()
                # GENERATES AND RETURN LIST OF CHILD STATE NODES
                children = node.generateChildren()
                for element in children:
                    # FOR EACH CHILD CREATED, CHECKS IF WE'VE SEEN THE STATE BEFORE,
                    # IF STATE HASN'T BEEN SEARCHED BEFORE, ITS ADDED TO SEARCH QUEUE
                    if element.getState not in checkedStates:
                        searchQueue.push(element)
            # IF STATE EQUALS GOAL STATE
            else:
                # print("you've solved the puzzle")
                # print(node.getKey())
                foundPath.push(node)
                while foundPath.size() > 0:
                    print(node.getKey())
                    if node.getKey() == 1:
                        solvePath.append(1)
                        break
                    key = node.getKey()
                    solvePath.append(key)
                    parentKey = node.getParentKey()
                    # print(parentKey)
                    # NodeList.print()
                    node = NodeList.get(parentKey)
                    # print(node.getKey)
                    foundPath.pop()
                    foundPath.push(node)
                for element in reversed(solvePath):
                    print("-----------------------------------------")
                    node = NodeList.get(element)
                    print()
                    print("Node Key:", node.getKey())
                    print("Node State:", node.getState())
                    print("Action:", node.getAction())
                    print("Cost:", node.getCost())
                    print()
                    printChildren(node.getState())
                break


##### -------------------------------------------
##### USER INTERFACE CODE
##### -------------------------------------------

while True:
    startNode = Node(1, EASY, 0, [], "Start", 1, 0)
    #bfs(startNode)
    dfs(startNode)
    userInput = input("what Program do you want to run?")
    if userInput == "yes":
        #  givenKey, givenState, givenParentKey, givenParentState, givenAction, givenDepth, givenCost
        startNode = Node(1, EASY, 0, [], "Start", 1, 0)
        bfs(startNode)
