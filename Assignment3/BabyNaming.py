# file_object  = open(“filename”, “mode”) where file_object is the variable to add the file object.
#GLOBAL VARS
CHAR_LIST = []

names = open("namesBoys.txt", "r")
names = names.read().splitlines()
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

def generateDataset():
    file = open("namesBoys.txt", "r")
    names = file.read().splitlines()
    for name in names:
        for letter in name:
            if letter.upper() not in CHAR_LIST:
                CHAR_LIST.append(letter.upper())





generateDataset()
for x in CHAR_LIST:
    print(x)