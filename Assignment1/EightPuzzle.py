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
    childrenKeys = []
    visited = False
    parentKey = 0
    parentState = []
    action = ""
    depth = 0
    cost = 0
    totalPathCost = 0

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

    def addTotalCost(self, x):
        self.totalPathCost += x

    def getParentState(self):
        return self.parentState

    def getAction(self):
        return self.action

    def setDepth(self, givenDepth):
        self.depth = givenDepth

    def getDepth(self):
        return self.depth

    def h1(self):
        h = 0
        state = self.getState()
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

    def h2(self):
        total = 0
        for x in self.getState():
            pos1 = self.getState().index(x)
            pos2 = GOAL.index(x)
            h = abs(pos1 - pos2)
            total = total + h
        return total

    def h3(self):
        total = 0
        for x in self.getState():
            pos1 = self.getState().index(x)
            pos2 = GOAL.index(x)
            h = abs(pos1 - pos2)
            total = ((total + h) * x)
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
                # global keyCounter
                KEY_COUNTER += 1
            childNode2 = Node(KEY_COUNTER, child2, self.key, self.state, action2, [], parentDepth + 1, cost2)
            tempChildList.append(childNode2)
        if child3 not in [self.state, self.parentState]:
            with threadLock:
                # global keyCounter
                KEY_COUNTER += 1
            childNode3 = Node(KEY_COUNTER, child3, self.key, self.state, action3, [], parentDepth + 1, cost3)
            tempChildList.append(childNode3)
        if child4 not in [self.state, self.parentState]:
            with threadLock:
                # global keyCounter
                KEY_COUNTER += 1
            childNode4 = Node(KEY_COUNTER, child4, self.key, self.state, action4, [], parentDepth + 1, cost4)
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

    def emptyStack(self):
        self.items.clear()


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

    def emptyGraph(self):
        self.dict.clear()


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
        # printChildren(node.getState())
        # print()
        # print(node.getKey(), ":", node.getState(), ":", node.getDepth())
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
                    # print(element.getKey(), ":", element.getState(), ":", element.getDepth())
                    # FOR EACH CHILD CREATED, CHECKS IF WE'VE SEEN THE STATE BEFORE,
                    # IF STATE HASN'T BEEN SEARCHED BEFORE, ITS ADDED TO SEARCH QUEUE
                    if element.getState() not in checkedStates:
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
                    print("Depth:", node.getDepth())
                    print("Cost:", node.getCost())
                    print()
                    printChildren(node.getState())
                return


def dfs(startNode):
    s = Stack()
    visitedStates = []
    NodeList = Graph()
    retracePath = Queue()
    foundPath = Stack()
    solvePath = []
    s.push(startNode)
    while s.size() > 0:
        print(s.size())
        node = s.pop()
        print(node.getState())
        if node.getState() in visitedStates:
            print("skipppppppppping")
            continue
        if node.getState() in visitedStates:
            print("fuckfuckfuckfuckfuckfuvkfvajksfdlkajflskjf")
        NodeList.add(node.getKey(), node)
        #print()
        #print(node.getKey(), ":", node.getState(), ":", node.getDepth())
        if node.getState() == GOAL:
            print("you have solved the puzzle")
            retracePath.push(node)
            foundPath.push(node)
            while foundPath.size() > 0:
                # print(node.getKey())
                if node.getKey() == 1:
                    solvePath.append(1)
                    break
                key = node.getKey()
                solvePath.append(key)
                parentKey = node.getParentKey()
                node = NodeList.get(parentKey)
                foundPath.pop()
                foundPath.push(node)
            for element in reversed(solvePath):
                print("-----------------------------------------")
                node = NodeList.get(element)
                print()
                print("Node Key:", node.getKey())
                print("Node State:", node.getState())
                print("Action:", node.getAction())
                print("Depth:", node.getDepth())
                print("Cost:", node.getCost())
                print()
                printChildren(node.getState())
            return
        if node.getVisited() == False:
            if node.getState() not in visitedStates:
                visitedStates.append(node.getState())
                node.setVisited()
                children = node.generateChildren()
                node.addChildren(children)
                for child in reversed(children):
                    key = child.getKey()
                    if key not in node.getChildKeys():
                        node.addChildKeys(key)
                        s.push(child)

        else:
            continue



def IterativeDeepening(startNode):
    currentDepth = 0
    maxDepth = 1
    s = Stack()
    NodeList = Graph()
    while currentDepth < 1000:
        maxDepth = maxDepth + 1
        NodeList.emptyGraph()
        s.emptyStack()
        retracePath = Queue()
        foundPath = Stack()
        solvePath = []
        s.push(startNode)
        while currentDepth <= maxDepth:
            if s.size() > 0:
                node = s.pop()
            else:
                break
            #currentDepth = node.getDepth()
            print(node.getKey(), ":", node.getState(), ":", node.getDepth())

            NodeList.add(node.getKey(), node)
            if node.getState() == GOAL:
                print("you have solved the puzzle")
                print(node.getDepth())
                retracePath.push(node)
                foundPath.push(node)
                while foundPath.size() > 0:
                    # print(node.getKey())
                    if node.getKey() == 1:
                        solvePath.append(1)
                        break
                    key = node.getKey()
                    solvePath.append(key)
                    parentKey = node.getParentKey()
                    node = NodeList.get(parentKey)
                    foundPath.pop()
                    foundPath.push(node)
                for element in reversed(solvePath):
                    print("-----------------------------------------")
                    node = NodeList.get(element)
                    print()
                    print("Node Key:", node.getKey())
                    print("Node State:", node.getState())
                    print("Action:", node.getAction())
                    print("Depth:", node.getDepth())
                    print("Cost:", node.getCost())
                    print()
                    printChildren(node.getState())
                return
            if node.getVisited() == True:
                continue
            NodeList.add(node.getKey(), node)
            if node.getDepth() < maxDepth:
                children = node.generateChildren()
                node.addChildren(children)
                for child in children:
                    if child.getState() != node.getState():
                        if child.getState() != node.getParentState():
                            key = child.getKey()
                            if key not in node.getChildKeys():
                                node.addChildKeys(key)
                                s.push(child)

def UniformCost(startNode):
    NodeList = Graph()
    visitedStates = []
    NodeQueue = Queue()
    NodeQueue.push(startNode)
    while NodeQueue.size() > 0:
        node = NodeQueue.pop()
        NodeList.add(node.getKey(), node)
       #print(node.getKey(), ":", node.getState(), ":", node.getDepth(), ":", node.getTotalPathCost())
        if node.getState() not in visitedStates:
            visitedStates.append(node)
            if node.getState() == GOAL:
                print("you found the goal!!")
                #print(node.getKey(), ":", node.getState(), ":", node.getDepth(), ":", node.getTotalPathCost())
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
                    # print(node.getKey(), ":", node.getState(), ":", node.getDepth(), ":", node.getCost(), ":", totalPathCost)
                    print("-----------------------------------------")
                    print()
                    print("Node Key:", node.getKey())
                    print("Node State:", node.getState())
                    print("Action:", node.getAction())
                    print("Depth:", node.getDepth())
                    print("Edge Cost:", node.getCost())
                    print("Total Cost:", totalPathCost)
                    print()
                    printChildren(node.getState())
                return
            children = node.generateChildren()
            for child in children:
                child.addTotalCost(child.getCost())
                if child.getState() not in visitedStates:
                    NodeQueue.push(child)

def Best(startNode):
    pass












##### -------------------------------------------
##### USER INTERFACE CODE
##### -------------------------------------------

while True:
    startNode = Node(1, MEDIUM, 0, [], "Start", [], 1, 0)
    # bfs(startNode)
    #dfs(startNode)
    #IterativeDeepening(startNode)
    UniformCost(startNode)
    Best(startNode)
    userInput = input("what Program do you want to run?")
    if userInput == "yes":
        #  givenKey, givenState, givenParentKey, givenParentState, givenAction, givenDepth, givenCost
        startNode = Node(1, EASY, 0, [], "Start", [], 1, 0)
        bfs(startNode)
