## Starting with things i know how to do that won't require research
## First gather list of words that need to be found
WordList = []
NextWord =input('Enter word to be added to search list, enter "Done!", without the quotation marks when complete:')
while NextWord != "Done!":
    WordList.append(NextWord.lower())
    NextWord = input('Enter word to be added to search list, enter "Done!", without the quotation marks when complete:')
## Build a dummy array to test word finding logic
DummyArrayofArrays = []
DummyArray1 = ["a", "b", "c", "d", "e"]
DummyArray2 = ["f", "g", "h", "i", "j"]
DummyArray3 = ["k", "l", "m", "n", "o"]
DummyArray4 = ["p", "q", "r", "s", "t"]
DummyArray5 = ["u", "v", "w", "x", "y"]
DummyArrayofArrays.append(DummyArray1)
DummyArrayofArrays.append(DummyArray2)
DummyArrayofArrays.append(DummyArray3)
DummyArrayofArrays.append(DummyArray4)
DummyArrayofArrays.append(DummyArray5)
## Get Possible lengths of words to search for
WordListLen = []
for Word in WordList:
    l = len(Word)
    if l not in WordListLen: ## deduplicate list
        WordListLen.append(l)
c = 0
d = 0
m = 0
RevStrSrch = ""
StrSrch = ""
xdim = len(DummyArrayofArrays[0]) ## determine X dimension by the length of the first array
ydim = len(DummyArrayofArrays) ## determine Y dimension by the length of the array of arrays
for WordLen in WordListLen: ## For each length of word on the word list, important for determining edges of grid
    for xloc in range(xdim): 
        for yloc in range(ydim):
            m += 1
            print(m) 
            if xloc + WordLen <= xdim: # horizontal search determine if the string will extend beyond the bounds of the grid
                c = 0 # reset iteration variable
                LSrch = "" # reset string search variables
                RSrch = ""
                while c < WordLen:
                    LSrch = LSrch + DummyArrayofArrays[yloc][xloc - c + WordLen - 1] # for horizontal and vertical searches we can search forward and backwards at the same tim
                    RSrch = RSrch + DummyArrayofArrays[yloc][xloc + c]
                    if RSrch in WordList and len(RSrch) == WordLen:
                        print(RSrch, "located at x:",xloc + 1,"y:",yloc + 1, "going right!")
                    if LSrch in WordList and len(LSrch) == WordLen:
                        print(LSrch, "located at x:",xloc + WordLen,"y:",yloc + 1, "going left!")
                    c += 1
            if yloc + WordLen <= ydim: # vertical search determine if the string will extend beyond the bounds of the grid
                c = 0 # reset iteration variable
                USrch = "" # reset string search variables
                DSrch = ""
                while c < WordLen: # search based on the length of the word
                    USrch = USrch + DummyArrayofArrays[yloc - c + WordLen - 1][xloc] 
                    DSrch = DSrch + DummyArrayofArrays[yloc + c][xloc]
                    if DSrch in WordList and len(DSrch) == WordLen:
                        print(DSrch, "located at x:",xloc + 1,"y:",yloc + 1, "going down!")
                    if USrch in WordList and len(USrch) == WordLen:
                        print(USrch, "located at x:",xloc + 1,"y:",yloc + WordLen, "going up!")
                    c += 1
            if yloc + WordLen <= ydim and xloc + WordLen <= xdim: # diagonal search determine if the string will extend beyond the bounds of the grid
                c = 0 # reset iteration variables
                DRSrch = ""
                while c < WordLen:
                    DRSrch = DRSrch + DummyArrayofArrays[yloc + c][xloc + c]
                    if DRSrch in WordList and len(DRSrch) == WordLen:
                        print(DRSrch, "located at x:",xloc + 1,"y:",yloc + 1, "going down and right!")
                    c += 1
            if yloc + 1 - WordLen >= 0 and xloc + 1 - WordLen >= 0:
                c = 0
                ULSrch = "" 
                while c < WordLen:
                    ULSrch = ULSrch + DummyArrayofArrays[yloc - c][xloc - c]
                    if ULSrch in WordList and len(ULSrch) == WordLen:
                        print(ULSrch, "located at x:",xloc + 1,"y:",yloc + 1, "going up and left!")
                    c += 1
            if yloc + WordLen <= ydim and xloc + 1 - WordLen >= 0:
                c = 0
                DLSrch = ""
                while c < WordLen:
                    DLSrch = DLSrch + DummyArrayofArrays[yloc + c][xloc - c]
                    if DLSrch in WordList and len(DLSrch) == WordLen:
                        print(DLSrch, "located at x:",xloc + 1,"y:",yloc + 1, "going up and right!")
                    c += 1
            if yloc + 1 - WordLen >= 0 and xloc + WordLen <= xdim:
                c = 0
                URSrch = ""
                while c < WordLen:
                    URSrch = URSrch + DummyArrayofArrays[yloc - c][xloc + c]
                    if URSrch in WordList and len(URSrch) == WordLen:
                        print(URSrch, "located at x:",xloc + 1,"y:",yloc + 1, "going down and left!")
                    c += 1