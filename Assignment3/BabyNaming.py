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
            if name[i+m] == "_":
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
        if character.getKey() == ("_"* m):
            for letter in character.getNextStrList():
                totalStartSegments.append(letter)
    randNum = randomNumber(len(totalStartSegments))
    return totalStartSegments[randNum]


def getLetter(segment, list):
    letters = []
    print(segment, "test")
    for character in list:
        if character.getKey() == segment:
            for letter in character.getNextStrList():
                letters.append(letter)
    print(letters)
    randNum = randomNumber(len(letters))
    #print(randNum)
    return letters[randNum]


def markov(list):
    global CURRENT_NAME
    startString = startSequence(CHAR_LIST)
    CURRENT_NAME = ("_" * m) + startString
    currentSegment = CURRENT_NAME[(len(CURRENT_NAME)-(m)):(len(CURRENT_NAME))]
    for i in range(MAX_LENGTH):
        letter = getLetter(currentSegment, CHAR_LIST)
        CURRENT_NAME = CURRENT_NAME + letter
        print(CURRENT_NAME)
        currentSegment = CURRENT_NAME[(len(CURRENT_NAME)-(m)):(len(CURRENT_NAME))]
        #print(currentSegment)







generateDataset()
markov(CHAR_LIST)
#startSequence(CHAR_LIST)
# for x in CHAR_LIST:
#     print(x.getKey(), x.getNextStrList())
