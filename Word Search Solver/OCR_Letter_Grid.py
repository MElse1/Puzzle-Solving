import pytesseract
import re

## This OCR is kind of janky.  The logic works! (But the actual OCR process which I'm not nearly a good enough programmer to make myself is just kinda bad) I tried multiple different 
## OCR solutions and they all had about the same eror rate. So I stuck with what I knew which was pytesseract.  The honest to  goodness best results I've seen with free off the shelf 
## OCR comes from the windows Snipping Tool text actions feature.  If the OCR of your word search is riddled with errors when it presents the grid for you to error check, I reccomend 
## just snipping the word search, and pasting it into the validation portion line by line, and deleting any extra lines.  That's actually what I ended up doing when I was
## troubleshooting this process, I just had the correct grid saved to a notepad file, and copied it in every time I tried the solution.

def OCRLG(x):
    done = 0
    while done != 1:
        print("Please enter the entire path to the word search letter grid, this can be done easily by right clicking the file in windows explorer, and selected 'Copy as Path'")
        print("remove the quotation marks that are added to the text")
        wordsearchlocation = x
        listofstrings = [] #empty lists for use later
        listofstrings2 = [] 
        listofstrings3 = []
        texttoadd = "" #empty string for use later
        word_search = pytesseract.image_to_boxes(wordsearchlocation) #function to OCR the word search
        for text in word_search: #iterate through each character because PyTesseract outputs as one long string, and input it into an array, each character in the pytesseract output is on it's own line
            if text == '\n':
                listofstrings.append(texttoadd)
                texttoadd = ""
            else:
                texttoadd = texttoadd + text  #if the character is not a new line character it adds it to the blank string variable, if it is a new line character it appends the string to a list
        for string in listofstrings:  #iterate through each string in the array
            splitlist = re.split("\s",string) #break the string into an array of strings for indexing purposes
            if len(splitlist[2]) < 2:  #all the if functions here are to make the strings the same length for sorting purposes
                splitlist[2] = str(0) + splitlist[2]
            if len(splitlist[2]) < 3:
                splitlist[2] = str(0) + splitlist[2]
            if len(splitlist[2]) < 4:
                splitlist[2] = str(0) + splitlist[2]
            if len(splitlist[1]) < 2:
                splitlist[1] = str(0) + splitlist[1]
            if len(splitlist[1]) < 3:
                splitlist[1] = str(0) + splitlist[1]
            if len(splitlist[1]) < 4:
                splitlist[1] = str(0) + splitlist[1]   
            texttoadd = "" + splitlist[2] + " " + splitlist[1] + " " + splitlist[0]  #append the vertical start position, horizontal end position, and the character to another list
            listofstrings2.append(texttoadd)
        splitlist = re.split("\s",listofstrings[0]) #break the string into an array of strings for indexing purposes
        if len(splitlist[2]) < 2: #normalize the values
            splitlist[2] = str(0) + splitlist[2]
        if len(splitlist[2]) < 3:
            splitlist[2] = str(0) + splitlist[2]
        if len(splitlist[2]) < 4:
            splitlist[2] = str(0) + splitlist[2]
        lastrow = splitlist[2] #assign lastrow to the vertical start position of the first character in the OCR output array
        listofstrings2.sort(reverse=True) #Sort the filterred output list with the highest vertical position first
        listofstrings = [] #discard the original OCR list
        for string in listofstrings2: #iterate through the filtered output list
            splitlist = []  #empty splitlist list
            splitlist = re.split("\s", string) #break the string into an array of strings for indexing purposes
            if lastrow <= splitlist[0] - 5 or lastrow >= splitlist[0] - 5:  # check to see if the vertical start position of the line has changed. The OCR measures in pixels, so the 
                listofstrings3.append(listofstrings)                        # + or - 5 should account for slightly diagonal grids
                listofstrings = []
            texttoadd = "" + splitlist[1] + " " + splitlist[2]  
            listofstrings.append(texttoadd) # if it has not, append the string to a list
            lastrow = splitlist[0] # set the value of lastrow to the vertical position of the current line
        i = 0
        listofstrings2 = []
        listofstrings = []
        for list in listofstrings3:
            listofstrings3[i].sort() # sort the lists within the list of lines by lowest number to highest
            for string in list:
                splitlist = splitlist = re.split("\s",string)
                texttoadd = splitlist[1].upper()
                listofstrings2.append(texttoadd)
                texttoadd = ""
            listofstrings.append(listofstrings2)
            listofstrings2 = []
            i += 1
        print("Verify the grid of letters scanned, where the top left of the grid scanned should be under the V at the start of this line")
        for list in listofstrings:
            print(list)
        print("And the bottom left of the grid should be above the A the start of this line.")
        verify = ""
        deletelist = []
        i = 1
        listofstrings3 = []
        for list in listofstrings:
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
                listofstrings2 = []
                listofstrings2 = re.split("\s",verify)
                listofstrings[i - 1] = listofstrings2
                i += 1
            for list in listofstrings:
                print(list)
            print("Deleted lines will be removed at the end")
        if deletelist != []:
            deletelist.sort(reverse=True)
            for number in deletelist:
                del listofstrings[number]
        for line in listofstrings:
            print(line)
        verify = input("If the above grid is correct, press enter, if it is not enter anything below")
        if verify == "":
            done = 1
            return(listofstrings)
        else:
            print("Letter grid creation failed, starting over")