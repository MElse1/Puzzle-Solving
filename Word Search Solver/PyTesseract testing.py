import pytesseract
import re

dictofstrings = []
dictofstrings2 = []
dictofstrings3 = []
texttoadd = ""
word_search = pytesseract.image_to_boxes("C:\\Users\\elseh\\OneDrive\\Pictures\\Screenshots\\Word Search.png")
for text in word_search:
    if text == '\n':
        dictofstrings.append(texttoadd)
        texttoadd = ""
    else:
        texttoadd = texttoadd + text
for string in dictofstrings:
    splitdict = []
    splitdict = re.split("\s",string)
    if len(splitdict[2]) < 2:
        splitdict[2] = str(0) + splitdict[2]
    if len(splitdict[2]) < 3:
        splitdict[2] = str(0) + splitdict[2]
    if len(splitdict[2]) < 4:
        splitdict[2] = str(0) + splitdict[2]
    if len(splitdict[1]) < 2:
        splitdict[1] = str(0) + splitdict[1]
    if len(splitdict[1]) < 3:
        splitdict[1] = str(0) + splitdict[1]
    if len(splitdict[1]) < 4:
        splitdict[1] = str(0) + splitdict[1]   
    texttoadd = "" + splitdict[2] + " " + splitdict[1] + " " + splitdict[0]
    dictofstrings2.append(texttoadd)
splitdict = []
splitdict = re.split("\s",dictofstrings[0])
if len(splitdict[2]) < 2:
    splitdict[2] = str(0) + splitdict[2]
if len(splitdict[2]) < 3:
    splitdict[2] = str(0) + splitdict[2]
if len(splitdict[2]) < 4:
    splitdict[2] = str(0) + splitdict[2]
lastrow = splitdict[2]
dictofstrings2.sort()
dictofstrings = []
for string in dictofstrings2:
    splitdict = []
    splitdict = re.split("\s", string)
    if lastrow == splitdict[0]:
        texttoadd = "" + splitdict[1] + " " + splitdict[2]
        dictofstrings.append(texttoadd)
    else:
        dictofstrings3.append(dictofstrings)
        lastrow = splitdict[0]
dictofstrings3.sort()
i = 0
for array in dictofstrings3:
    print(len(dictofstrings3[i]))
    print(dictofstrings3[i])
    i += 1
print(i)