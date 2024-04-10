import pytesseract
import re

## as an aside, I understand that none of these are dictionaries, they are all lists, I just started with the dictofstrings variablename and didn't realize that that was an incorrect
## description of what they are until I was way to far into this to go back and change it
def OCRLG(x):
    done = 0
    while done != 1:
        print("Please enter the entire path to the word search letter grid, this can be done easily by right clicking the file in windows explorer, and selected 'Copy as Path'")
        print("remove the quotation marks that are added to the text")
        wordsearchlocation = x
        dictofstrings = [] #empty lists for use later
        dictofstrings2 = [] 
        dictofstrings3 = []
        texttoadd = "" #empty string for use later
        word_search = pytesseract.image_to_boxes(wordsearchlocation) #function to OCR the word search
        for text in word_search: #iterate through each character because PyTesseract outputs as one long string, and input it into an array, each character in the pytesseract output is on it's own line
            if text == '\n':
                dictofstrings.append(texttoadd)
                texttoadd = ""
            else:
                texttoadd = texttoadd + text  #if the character is not a new line character it adds it to the blank string variable, if it is a new line character it appends the string to a dictionary
        for string in dictofstrings:  #iterate through each string in the array
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
            if lastrow != splitdict[0]: # check to see if the vertical start position of the line has changed
                dictofstrings3.append(dictofstrings)
                dictofstrings = []
            texttoadd = "" + splitdict[1] + " " + splitdict[2]  
            dictofstrings.append(texttoadd) # if it has not, append the string to a list
            lastrow = splitdict[0] # set the value of lastrow to the vertical position of the current line
        i = 0
        dictofstrings2 = []
        dictofstrings = []
        for list in dictofstrings3:
            dictofstrings3[i].sort() # sort the lists within the list of lines by lowest number to highest
            for string in list:
                splitdict = splitdict = re.split("\s",string)
                texttoadd = splitdict[1].upper()
                dictofstrings2.append(texttoadd)
                texttoadd = ""
            dictofstrings.append(dictofstrings2)
            dictofstrings2 = []
            i += 1
        print("Verify the grid of letters scanned, where the top left of the grid scanned should be under the V at the start of this line")
        for list in dictofstrings:
            print(list)
        print("And the bottom left of the grid should be above the A the start of this line.")
        verify = ""
        deletelist = []
        i = 1
        dictofstrings3 = []
        for list in dictofstrings:
            print("Line:", i, "is", list)
            print("check the order of the letters and if incorrect input the letters with or without a space between them")
            print("Only enter the letter and spaces!!! Note: if there are any errors the entire line must be re-entered")
            print("if the entire line should be deleted enter 'DELETE', if the line is correct press enter without entering anything")
            verify = input()
            verify = verify.upper()
            print(verify)
            if verify == "" :
                i += 1
            elif verify == "DELETE":
                deletelist.append(i-1)
            else:
                dictofstrings2 = []
                dictofstrings2 = re.split("\s",verify)
                dictofstrings[i - 1] = dictofstrings2
                i += 1
            for list in dictofstrings:
                print(list)
            print("Deleted lines will be removed at the end")
        if deletelist != []:
            deletelist.sort(reverse=True)
            for number in deletelist:
                del dictofstrings[number]
        for line in dictofstrings:
            print(line)
        verify = input("If the above grid is correct, press enter, if it is not enter anything below")
        if verify == "":
            done = 1
            return(dictofstrings)
        else:
            print("Letter grid creation failed, starting over")