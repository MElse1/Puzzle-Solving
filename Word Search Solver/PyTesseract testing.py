import pytesseract
import re

## as an aside, I understand that none of these are dictionaries, they are all lists, I just started with the dictofstrings variablename and didn't realize that that was an incorrect
## description of what they are until I was way to far into this to go back and change it

dictofstrings = [] #empty list for use later
dictofstrings2 = [] 
dictofstrings3 = []
texttoadd = "" #empty string for use later
word_search = pytesseract.image_to_boxes("C:\\Users\\elseh\\OneDrive\\Pictures\\Screenshots\\Word Search.png") #function to OCR the word search
for text in word_search: #iterate through each character because PyTesseract outputs as one long string, and input it into an array, each character in the pytesseract output is on it's own line
    if text == '\n':
        dictofstrings.append(texttoadd)
        texttoadd = ""
    else:
        texttoadd = texttoadd + text  #if the character is not a new line character it adds it to the blank string variable, if it is a new line character it appends the string to a dictionary
for string in dictofstrings:  #iterate through each string in the array
    splitdict = []  
    splitdict = re.split("\s",string) #break the string into an array of strings for indexing purposes
    if len(splitdict[2]) < 2:  #all the if functions here are to make the strings the same length for sorting purposes
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
    texttoadd = "" + splitdict[2] + " " + splitdict[1] + " " + splitdict[0]  #append the vertical start position, horizontal end position, and the character to another dictionary
    dictofstrings2.append(texttoadd)
splitdict = [] # empty splitdict varaible array 
splitdict = re.split("\s",dictofstrings[0]) #break the string into an array of strings for indexing purposes
if len(splitdict[2]) < 2: #normalize the values
    splitdict[2] = str(0) + splitdict[2]
if len(splitdict[2]) < 3:
    splitdict[2] = str(0) + splitdict[2]
if len(splitdict[2]) < 4:
    splitdict[2] = str(0) + splitdict[2]
lastrow = splitdict[2] #assign lastrow to the vertical start position of the first character in the OCR output array
dictofstrings2.sort(reverse=True) #Sort the filterred output list with the highest vertical position first
dictofstrings = [] #discard the original OCR list
for string in dictofstrings2: #iterate through the filtered output list
    splitdict = []  #empty splitdict list
    splitdict = re.split("\s", string) #break the string into an array of strings for indexing purposes
    if lastrow == splitdict[0]: # check to see if the vertical start position of the line has changed
        texttoadd = "" + splitdict[1] + " " + splitdict[2]  
        dictofstrings.append(texttoadd) # if it has not, append the string to a list
        lastrow = splitdict[0] # set the value of lastrow to the vertical position of the current line
    else:
        dictofstrings3.append(dictofstrings) #if it has not, append the list to a list
i = 0
for list in dictofstrings3:
    dictofstrings3[i].sort(reverse=True) # sort the lists within the list of lines by lowest number to highest
    i += 1
    print(dictofstrings3[i])