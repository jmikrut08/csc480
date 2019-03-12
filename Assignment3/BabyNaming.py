# file_object  = open(“filename”, “mode”) where file_object is the variable to add the file object.
#GLOBAL VARS
CHAR_LIST = []

#names = open("namesBoys.txt", "r")
#names = names.read().splitlines()
#for x in names:
    #x = "__" + x + "__"
    #print(x)
# for line in names:
#     line = line.splitlines()
# #    line = "__" + line + "__"
#     print(line)


# def count_char(list, char):
#     totalcount = 0
#     for name in names:
#         for letter in name:
#             if letter == char:
#                 totalcount += 1
#     return totalcount
#
# rCount = count_char(names, "r")
# print(rCount)


class Pair:
    char = ""
    count = 0

    def __init__(self, charIn, countIn):
        self.char = charIn
        self.count = countIn

    def getChar(self):
        return self.char

    def getCount(self):
        return self.count

    def addCount(self):
        self.count += 1

class Character:
    letter = ""
    nextLetter = [] # list of pairs

    def __init__(self, letterIn, nextLetterIn):
        self.letter = letterIn
        self.nextLetter = nextLetterIn

    def getKey(self):
        return self.letter

    def getPairList(self):
        return self.nextLetter

    def addPair(pair): # only works if letter isn't in list yet
        listEdited = 0
        for x in nextLetter:
            if x.getChar() == pair.getChar():
                x.addCount()
                listEdited = 1
        if listEdited == 0:
            self.nextLetter.append(pair)

def characterInList(list,letter):
    for x in list: # list of Characters
        if x.getKey() == letter:
            return True
    return False

def appendPair(list, pair):
    pass

def generateDataset():
    file = open("namesBoys.txt", "r")
    names = file.read().splitlines()
    for name in names:
        name = "__" + name + "__"
        #print(name)
        index = 0
        for i in range(len(name)):
            if (characterInList(CHAR_LIST, name[i].upper())) == False:
                newCharacter = Character(name[i].upper(), [])
                CHAR_LIST.append(newCharacter)







generateDataset()
for x in CHAR_LIST:
    print(x.getKey(), x.getPairList())