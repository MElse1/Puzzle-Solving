## Starting with things i know how to do that won't require research
## First gather list of words that need to be found
WordList = []
NextWord =input('Enter word to be added to search list, enter "Done!", without the quotation marks when complete:')
while NextWord != "Done!":
    WordList.append(NextWord.lower())
    NextWord = input('Enter word to be added to search list, enter "Done!", without the quotation marks when complete:')
## Build a dummy array to test word finding logic
DummyArrayofArrays = []
DummyArray1 = ["c", "a", "p", "e"]
DummyArray2 = ["a", "a", "p", "g"]
DummyArray3 = ["r", "a", "e", "g"]
DummyArray4 = ["e", "a", "p", "s"]
DummyArrayofArrays.append(DummyArray1)
DummyArrayofArrays.append(DummyArray2)
DummyArrayofArrays.append(DummyArray3)
DummyArrayofArrays.append(DummyArray4)
## Get Possible lengths of words to search for
WordListLen = []
for Word in WordList:
    l = len(Word)
    if l not in WordListLen: ## deduplicate list
        WordListLen.append(l)
c = 0
d = 0
RevStrSrch = ""
StrSrch = ""
xdim = len(DummyArrayofArrays[0]) # determine X dimension by the length of the first array
ydim = len(DummyArrayofArrays) # determine Y dimension by the length of the array of arrays
for WordLen in WordListLen: ## For each length of word on the word list, important for determining edges of grid
    for xloc in range(xdim): 
        for yloc in range(ydim): 
            if xloc + WordLen <= xdim: # horizontal search determine if the string will extend beyond the bounds of the grid
                c = 0 # reset iteration variable
                LSrch = "" # reset reverse and forward string search variables
                RSrch = ""
                while c < WordLen:
                    LSrch = LSrch + DummyArrayofArrays[yloc][xloc - c - 1]
                    RSrch = RSrch + DummyArrayofArrays[yloc][xloc + c]
                    if RSrch in WordList and len(RSrch) == WordLen:
                        print(RSrch, "located at x:",xloc + 1,"y:",yloc + 1, "going right!")
                    if LSrch in WordList and len(LSrch) == WordLen:
                        print(LSrch, "located at x:",xdim - xloc,"y:",yloc + 1, "going left!")
                    c += 1
            if yloc + WordLen <= ydim: # vertical search determine if the string will extend beyond the bounds of the grid
                c = 0 # reset iteration variable
                USrch = "" # reset reverse and forward string search variables
                LSrch = ""
                while c < WordLen:
                    RevStrSrch = RevStrSrch + DummyArrayofArrays[yloc - c - 1][xloc]
                    StrSrch = StrSrch + DummyArrayofArrays[yloc + c][xloc]
                    if StrSrch in WordList and len(StrSrch) == WordLen:
                        print(StrSrch, "located at x:",xloc + 1,"y:",yloc + 1, "going down!")
                    if RevStrSrch in WordList and len(StrSrch) == WordLen:
                        print(StrSrch, "located at x:",xloc + 1,"y:",ydim - yloc, "going left!")
                    c += 1
            if yloc + WordLen <= ydim: # diagonal search determine if the string will extend beyond the bounds of the grid
                c = 0 # reset iteration variables
                ULSrch = "" # reset reverse and forward string search variables
                URSrch = ""
                while c < WordLen:
                    RevStrSrch = RevStrSrch + DummyArrayofArrays[yloc - c - 1][xloc]
                    StrSrch = StrSrch + DummyArrayofArrays[yloc + c][xloc]
                    if StrSrch in WordList and len(StrSrch) == WordLen:
                        print(StrSrch, "located at x:",xloc + 1,"y:",yloc + 1, "going down!")
                    if RevStrSrch in WordList and len(StrSrch) == WordLen:
                        print(StrSrch, "located at x:",xloc + 1,"y:",ydim - yloc, "going left!")
                    c += 1