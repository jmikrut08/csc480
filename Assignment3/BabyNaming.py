import random
# file_object  = open(“filename”, “mode”) where file_object is the variable to add the file object.
#GLOBAL VARS
CHAR_LIST = []
m = 2
MIN_LENGTH = 5
MAX_LENGTH = 10
CURRENT_NAME = ""

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


def generateDataset():
    global CHAR_LIST
    file = open("namesBoys.txt", "r")
    names = file.read().splitlines()
    for name in names:
        name = ("_" * m) + name + ("_" * m)
        #print(name)
        for i in range(len(name)):
            if (characterInList(CHAR_LIST, name[i:i+m].upper())) == False:
                newCharacter = Character(name[i:i+m].upper(), [])
                CHAR_LIST.append(newCharacter)
            if name[i] == "_" and i > m:
                #indexEnd = getCharacterIndex(CHAR_LIST, "_")
                #addLetterToIndex(CHAR_LIST, indexEnd, "_")
                break
            else:
                index = getCharacterIndex(CHAR_LIST, name[i:i+m].upper())
                addLetterToIndex(CHAR_LIST, index, name[i+m].upper())

# -----------------------------------------------------------------------------#
# ----------------------------- Name Generation -------------------------------#
# -----------------------------------------------------------------------------#

def randomNumber(length):
    num = random.randint(0, length-1)
    return num

def startSequence(list):
    totalStartSegments = []
    for character in list:
        if character.getKey() == ("_" * m):
            for letter in character.getNextStrList():
                totalStartSegments.append(letter)
    randNum = randomNumber(len(totalStartSegments))
    return totalStartSegments[randNum]


def getLetter(segment, list):
    letters = []
    for character in list:
        if character.getKey() == segment:
            for letter in character.getNextStrList():
                letters.append(letter)
    if len(letters) < 1:
        return "_"
    randNum = randomNumber(len(letters))
    return letters[randNum]


def markov(list):
    global CURRENT_NAME
    startString = startSequence(CHAR_LIST)
    CURRENT_NAME = ("_" * m) + startString
    currentSegment = CURRENT_NAME[(len(CURRENT_NAME)-(m)):(len(CURRENT_NAME))]
    for i in range(MAX_LENGTH):
        #print(CURRENT_NAME)
        #print(currentSegment)
        letter = getLetter(currentSegment, CHAR_LIST)
        CURRENT_NAME = CURRENT_NAME + letter
        currentSegment = CURRENT_NAME[(len(CURRENT_NAME)-(m)):(len(CURRENT_NAME))]
    return CURRENT_NAME






generateDataset()
startSequence(CHAR_LIST)
# for x in CHAR_LIST:
#     print(x.getKey(), x.getNextStrList())
name = markov(CHAR_LIST)
print(name)
name = name[m:len(name)]
print(name)
finalName = ""
for i in range(len(name)):
    if name[i] == "_":
        break
    else:
        finalName = finalName + name[i]
print(finalName)
#startSequence(CHAR_LIST)
# for x in CHAR_LIST:
#     print(x.getKey(), x.getNextStrList())
