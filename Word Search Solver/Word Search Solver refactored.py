import OCR_Letter_Grid as OCR
## Starting with things i know how to do that won't require research
## First gather list of words that need to be found
WordList = []
FoundWords = []
NextWord =input('Enter word to be added to search list')
while NextWord != "Done!":
    NextWord.strip() # Remove whitespace
    WordList.append(NextWord.upper()) # standardize all text to upper case
    NextWord = input('Enter word to be added to search list, enter "Done!", without the quotation marks when complete:')
## Build a dummy array to test word finding logic
print("Enter the path to the picture of the letter grid")
print("The easiest way to do this is to right click the file and select 'Copy as Path'")
print("Make sure you remove the 's from the paste")
x = input()
listofstrings = []
listofstrings = OCR.OCRLG(x)
## Get Possible lengths of words to search for
WordListLen = []
for Word in WordList:
    l = len(Word)
    if l not in WordListLen: ## deduplicate list
        WordListLen.append(l)
RevStrSrch = ""
StrSrch = ""
xdim = len(listofstrings[0]) ## determine X dimension by the length of the first array
ydim = len(listofstrings) ## determine Y dimension by the length of the array of arrays
for WordLen in WordListLen: ## For each length of word on the word list, important for determining edges of grid
    for xloc in range(xdim): 
        for yloc in range(ydim):
            if xloc + WordLen <= xdim: # horizontal search determine if the string will extend beyond the bounds of the grid
                c = 0 # reset iteration variable
                LSrch = "" # reset string search variables for each loop
                RSrch = ""
                while c < WordLen: 
                    LSrch = LSrch + listofstrings[yloc][xloc - c + WordLen - 1] # for horizontal and vertical searches we can search forward and backwards at the same tim
                    RSrch = RSrch + listofstrings[yloc][xloc + c] 
                    if RSrch in WordList and len(RSrch) == WordLen: # if the search string matches a term on the list, the length check is to prevent double matches like cap/cape
                        FoundWords.append(RSrch)
                        print(RSrch, "located at x:",xloc + 1,"y:",yloc + 1, "going right!")    #! debating if I should reverse the Y coordinates, because as is (0,0) is the top left
                    if LSrch in WordList and len(LSrch) == WordLen:                             #! and most people would picture (0,0) as the bottom right left.
                        FoundWords.append(LSrch)
                        print(LSrch, "located at x:",xloc + WordLen,"y:",yloc + 1, "going left!")
                    c += 1
            if yloc + WordLen <= ydim: # vertical search determine if the string will extend beyond the bounds of the grid
                c = 0 
                USrch = "" 
                DSrch = ""
                while c < WordLen: 
                    USrch = USrch + listofstrings[yloc - c + WordLen - 1][xloc] 
                    DSrch = DSrch + listofstrings[yloc + c][xloc]
                    if DSrch in WordList and len(DSrch) == WordLen:
                        FoundWords.append(DSrch)
                        print(DSrch, "located at x:",xloc + 1,"y:",yloc + 1, "going down!")
                    if USrch in WordList and len(USrch) == WordLen:
                        FoundWords.append(USrch)
                        print(USrch, "located at x:",xloc + 1,"y:",yloc + WordLen, "going up!")
                    c += 1
            if yloc + WordLen <= ydim and xloc + WordLen <= xdim: # diagonal search determine if the string will extend beyond the bounds of the grid
                c = 0 
                DRSrch = ""
                while c < WordLen:
                    DRSrch = DRSrch + listofstrings[yloc + c][xloc + c]
                    if DRSrch in WordList and len(DRSrch) == WordLen:
                        FoundWords.append(DRSrch)
                        print(DRSrch, "located at x:",xloc + 1,"y:",yloc + 1, "going down and right!")
                    c += 1
            if yloc + 1 - WordLen >= 0 and xloc + 1 - WordLen >= 0:
                c = 0
                ULSrch = "" 
                while c < WordLen:
                    ULSrch = ULSrch + listofstrings[yloc - c][xloc - c]
                    if ULSrch in WordList and len(ULSrch) == WordLen:
                        FoundWords.append(ULSrch)
                        print(ULSrch, "located at x:",xloc + 1,"y:",yloc + 1, "going up and left!")
                    c += 1
            if yloc + WordLen <= ydim and xloc + 1 - WordLen >= 0:
                c = 0
                DLSrch = ""
                while c < WordLen:
                    DLSrch = DLSrch + listofstrings[yloc + c][xloc - c]
                    if DLSrch in WordList and len(DLSrch) == WordLen:
                        FoundWords.append(DLSrch)
                        print(DLSrch, "located at x:",xloc + 1,"y:",yloc + 1, "going up and right!")
                    c += 1
            if yloc + 1 - WordLen >= 0 and xloc + WordLen <= xdim:
                c = 0
                URSrch = ""
                while c < WordLen:
                    URSrch = URSrch + listofstrings[yloc - c][xloc + c]
                    if URSrch in WordList and len(URSrch) == WordLen:
                        FoundWords.append(URSrch)
                        print(URSrch, "located at x:",xloc + 1,"y:",yloc + 1, "going down and left!")
                    c += 1
print("Note that coordinate x: 1, y: 1 is the top left corner")
if len(WordList) == len(FoundWords):
    print("All words located!")
else:
    print(len(WordList) - len(FoundWords),"Words not found, They are:")
    for word in WordList:
        if word not in FoundWords:
            print(word)