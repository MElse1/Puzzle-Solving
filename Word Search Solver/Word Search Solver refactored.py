## Starting with things i know how to do that won't require research
## First gather list of words that need to be found
WordList = []
NextWord =input('Enter word to be added to search list, enter "Done!", without the quotation marks when complete:')
while NextWord != "Done!":
    WordList.append(NextWord.lower())
    NextWord = input('Enter word to be added to search list, enter "Done!", without the quotation marks when complete:')
## Build a dummy array to test word finding logic
## Get Possible lengths of words to search for
WordListLen = []
for Word in WordList:
    l = len(Word)
    if l not in WordListLen: ## deduplicate list
        WordListLen.append(l)
RevStrSrch = ""
StrSrch = ""
xdim = len(dictofstrings[0]) ## determine X dimension by the length of the first array
ydim = len(dictofstrings) ## determine Y dimension by the length of the array of arrays
for WordLen in WordListLen: ## For each length of word on the word list, important for determining edges of grid
    for xloc in range(xdim): 
        for yloc in range(ydim): 
            if xloc + WordLen <= xdim: # horizontal search determine if the string will extend beyond the bounds of the grid
                c = 0 # reset iteration variable
                LSrch = "" # reset string search variables for each loop
                RSrch = ""
                while c < WordLen: 
                    LSrch = LSrch + dictofstrings[yloc][xloc - c + WordLen - 1] # for horizontal and vertical searches we can search forward and backwards at the same tim
                    RSrch = RSrch + dictofstrings[yloc][xloc + c] 
                    if RSrch in WordList and len(RSrch) == WordLen: # if the search string matches a term on the list, the length check is to prevent double matches like cap/cape
                        print(RSrch, "located at x:",xloc + 1,"y:",yloc + 1, "going right!")    #! debating if I should reverse the coordinates, because as is (0,0) is the top right
                    if LSrch in WordList and len(LSrch) == WordLen:                             #! and most people would picture (0,0) as the bottom right point.
                        print(LSrch, "located at x:",xloc + WordLen,"y:",yloc + 1, "going left!")
                    c += 1
            if yloc + WordLen <= ydim: # vertical search determine if the string will extend beyond the bounds of the grid
                c = 0 
                USrch = "" 
                DSrch = ""
                while c < WordLen: 
                    USrch = USrch + dictofstrings[yloc - c + WordLen - 1][xloc] 
                    DSrch = DSrch + dictofstrings[yloc + c][xloc]
                    if DSrch in WordList and len(DSrch) == WordLen:
                        print(DSrch, "located at x:",xloc + 1,"y:",yloc + 1, "going down!")
                    if USrch in WordList and len(USrch) == WordLen:
                        print(USrch, "located at x:",xloc + 1,"y:",yloc + WordLen, "going up!")
                    c += 1
            if yloc + WordLen <= ydim and xloc + WordLen <= xdim: # diagonal search determine if the string will extend beyond the bounds of the grid
                c = 0 
                DRSrch = ""
                while c < WordLen:
                    DRSrch = DRSrch + dictofstrings[yloc + c][xloc + c]
                    if DRSrch in WordList and len(DRSrch) == WordLen:
                        print(DRSrch, "located at x:",xloc + 1,"y:",yloc + 1, "going down and right!")
                    c += 1
            if yloc + 1 - WordLen >= 0 and xloc + 1 - WordLen >= 0:
                c = 0
                ULSrch = "" 
                while c < WordLen:
                    ULSrch = ULSrch + dictofstrings[yloc - c][xloc - c]
                    if ULSrch in WordList and len(ULSrch) == WordLen:
                        print(ULSrch, "located at x:",xloc + 1,"y:",yloc + 1, "going up and left!")
                    c += 1
            if yloc + WordLen <= ydim and xloc + 1 - WordLen >= 0:
                c = 0
                DLSrch = ""
                while c < WordLen:
                    DLSrch = DLSrch + dictofstrings[yloc + c][xloc - c]
                    if DLSrch in WordList and len(DLSrch) == WordLen:
                        print(DLSrch, "located at x:",xloc + 1,"y:",yloc + 1, "going up and right!")
                    c += 1
            if yloc + 1 - WordLen >= 0 and xloc + WordLen <= xdim:
                c = 0
                URSrch = ""
                while c < WordLen:
                    URSrch = URSrch + dictofstrings[yloc - c][xloc + c]
                    if URSrch in WordList and len(URSrch) == WordLen:
                        print(URSrch, "located at x:",xloc + 1,"y:",yloc + 1, "going down and left!")
                    c += 1