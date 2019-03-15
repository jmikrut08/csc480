import random


#GLOBAL VARS
CHAR_LIST = [] # data list
m = 2           # markov order
MIN_LENGTH = 5  #input min length
MAX_LENGTH = 10 # input max length
CURRENT_NAME = ""   #name being generated
NAME_LIST = []  #list of all names in database to check if its unique


class Character:
    str = ""
    nextStr = [] # list of pairs

    def __init__(self, strIn, nextStrIn):
        self.str = strIn
        self.nextStr = nextStrIn

    def getKey(self):
        return self.str

    def getNextStrList(self):
        return self.nextStr

    def addLetter(self, string):
        self.nextStr.append(string)


# -----------------------------------------------------------------------------#
# --------------------- Creating original dataset -----------------------------#
# -----------------------------------------------------------------------------#


def characterInList(list,string): # boolean to see if letter is already present in CHAR_LIST
    for x in list: # list of Characters
        if x.getKey() == string:
            return True
    return False

def getCharacterIndex(list, string): # get index of of chacter in CHAR_LIST
    for i in range(len(list)):
        if list[i].getKey() == string:
            return i
    return 0

def addLetterToIndex(list, index, string): # adds letter to indexed Character in CHAR_LIST
    list[index].addLetter(string)


def generateDataset(gender): # reads data and sorts by markov order
    global CHAR_LIST
    global NAME_LIST
    file = open(gender, "r")
    names = file.read().splitlines()
    for name in names:
        NAME_LIST.append(name)
        name = ("_" * m) + name + ("_" * m)
        for i in range(len(name)):
            if (characterInList(CHAR_LIST, name[i:i+m].upper())) == False:
                newCharacter = Character(name[i:i+m].upper(), [])
                CHAR_LIST.append(newCharacter)
            if name[i] == "_" and i > m:
                break
            else:
                index = getCharacterIndex(CHAR_LIST, name[i:i+m].upper())
                addLetterToIndex(CHAR_LIST, index, name[i+m].upper())

# -----------------------------------------------------------------------------#
# ----------------------------- Name Generation -------------------------------#
# -----------------------------------------------------------------------------#

def randomNumber(length): # generates random number
    num = random.randint(0, length-1)
    return num

def startSequence(list): # selects first letter of name
    totalStartSegments = []
    for character in list:
        if character.getKey() == ("_" * m):
            for letter in character.getNextStrList():
                totalStartSegments.append(letter)
    randNum = randomNumber(len(totalStartSegments))
    return totalStartSegments[randNum]

def getLetter(segment, list): # gets next letter of name
    letters = []
    for character in list:
        if character.getKey() == segment:
            for letter in character.getNextStrList():
                letters.append(letter)
    if len(letters) < 1:
        return "_"
    randNum = randomNumber(len(letters))
    return letters[randNum]

def markov(list): # builds name
    global CURRENT_NAME
    startString = startSequence(CHAR_LIST)
    CURRENT_NAME = ("_" * m) + startString
    currentSegment = CURRENT_NAME[(len(CURRENT_NAME)-(m)):(len(CURRENT_NAME))]
    for i in range(MAX_LENGTH):
        letter = getLetter(currentSegment, CHAR_LIST)
        CURRENT_NAME = CURRENT_NAME + letter
        currentSegment = CURRENT_NAME[(len(CURRENT_NAME)-(m)):(len(CURRENT_NAME))]
    return CURRENT_NAME

# -----------------------------------------------------------------------------#
# ----------------------------- USER INTERFACE --------------------------------#
# -----------------------------------------------------------------------------#

def cleanName(name):
    finalName = ""
    name = name[m:len(name)]
    for i in range(len(name)):
        if name[i] == "_":
            break
        else:
            finalName = finalName + name[i]
    return finalName

# gender = input("Do you want to generate a boys name or girls name?\n1). MALE\n2). FEMALE\n")
# maxLength = input("What is the maximum Length of a desired name")
# minLength = input("What is the minimum Length of a desired name")
# order = input("What order of Markov model do you wish to use?")
# numberOfNames = input("How many names do you want to generate?")

gender = ""
maxLength = ""
minLength = ""
order = ""
numberOfNames = ""
nameList = []

possibleInts = ["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20"]

while True:
    gender = input("Do you want to generate a boys name or girls name?\n1). MALE\n2). FEMALE\n")
    if gender == "MALE" or gender == "1":
        gender = "namesBoys.txt"
        break
    if gender == "FEMALE" or gender == "2":
        gender = "namesGirls.txt"
        break
while True:
    maxLength = input("What is the maximum Length of a desired name\n")
    if maxLength in possibleInts:
        maxLength_int = int(maxLength)
        break
while True:
    minLength = input("What is the minimum Length of a desired name\n")
    if minLength in possibleInts:
        minLength_int = int(minLength)
        break
while True:
    order = input("What order of Markov model do you wish to use?\n")
    if order in possibleInts:
        order_int = int(order)
        break
while True:
    numberOfNames = input("How many names do you want to generate?\n")
    if numberOfNames in possibleInts:
        numberOfNames_int = int(numberOfNames)
        break

# update global variables
m = order_int   #markov model order
MIN_LENGTH = minLength_int # max length of name
MAX_LENGTH = maxLength_int + (2 * order_int) # min length of name

generateDataset(gender) # reads document and sorts data
startSequence(CHAR_LIST) # randomly chooses start letter from "__"

while len(nameList) < numberOfNames_int: # runs until generates enough names of proper length
    name = markov(CHAR_LIST)
    name = cleanName(name)

    if len(name) >= MIN_LENGTH and len(name) <= MAX_LENGTH-(2 * order_int): # checks if generated name is long enough and not in lists
        if name not in NAME_LIST and name not in nameList:
            nameList.append(name)
#print(NAME_LIST)
print(nameList)