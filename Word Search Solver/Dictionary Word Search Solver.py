import OCR_Letter_Grid as OCR
import enchant

FoundWords = 0
while True:
    try:
        MinLength = int(input("""The minimum length of word you want to find:"""))
        break
    except:
        print("Please enter a number!  (IE: 4, 3, 12)")
WordList = enchant.Dict("en_US")
print("Enter the path to the picture of the letter grid")
print("The easiest way to do this is to right click the file and select 'Copy as Path'")
print("""Make sure you remove 's or "s from the path, we just need the path (IE: C:\lettergrid.png)""")
x = input()
listofstrings = []
listofstrings = OCR.OCRLG(x)
## Get Possible lengths of words to search for
xdim = len(listofstrings[0]) ## determine X dimension by the length of the first array
ydim = len(listofstrings) ## determine Y dimension by the length of the array of arrays
for WordLen in range(MinLength,max(ydim,xdim)): ## For each length of word from the minimum length desired, to the largest dimension of the grid
    for xloc in range(xdim): 
        for yloc in range(ydim):
            if xloc + WordLen <= xdim: # horizontal search determine if the string will extend beyond the bounds of the grid
                c = 0 # reset iteration variable
                LSrch = "" # reset string search variables for each loop
                RSrch = ""
                while c < WordLen: 
                    LSrch = LSrch + listofstrings[yloc][xloc - c + WordLen - 1] # for horizontal and vertical searches we can search forward and backwards at the same time
                    RSrch = RSrch + listofstrings[yloc][xloc + c] 
                    if len(RSrch) == WordLen and WordList.check(RSrch): # if the search string matches a term on the list, the length check is to prevent double matches like cap/cape
                        print(RSrch, "located at x:",xloc + 1,"y:",yloc + 1, "going right!")
                        FoundWords += 1                                                              #! debating if I should reverse the Y coordinates, because as is (1,1) is the top left
                    if len(LSrch) == WordLen and WordList.check(LSrch):                              #! and most people would picture (1,1) as the bottom right.
                        print(LSrch, "located at x:",xloc + WordLen,"y:",yloc + 1, "going left!")
                        FoundWords += 1
                    c += 1
            if yloc + WordLen <= ydim: # vertical search determine if the string will extend beyond the bounds of the grid
                c = 0 
                USrch = "" 
                DSrch = ""
                while c < WordLen: 
                    USrch = USrch + listofstrings[yloc - c + WordLen - 1][xloc] 
                    DSrch = DSrch + listofstrings[yloc + c][xloc]
                    if len(DSrch) == WordLen and WordList.check(DSrch):
                        print(DSrch, "located at x:",xloc + 1,"y:",yloc + 1, "going down!")
                        FoundWords += 1
                    if len(USrch) == WordLen and WordList.check(USrch):
                        print(USrch, "located at x:",xloc + 1,"y:",yloc + WordLen, "going up!")
                        FoundWords += 1
                    c += 1
            if yloc + WordLen <= ydim and xloc + WordLen <= xdim: # diagonal search determine if the string will extend beyond the bounds of the grid
                c = 0 
                DRSrch = ""
                while c < WordLen:
                    DRSrch = DRSrch + listofstrings[yloc + c][xloc + c]
                    if len(DRSrch) == WordLen and WordList.check(DRSrch):
                        print(DRSrch, "located at x:",xloc + 1,"y:",yloc + 1, "going down and right!")
                        FoundWords += 1
                    c += 1
            if yloc + 1 - WordLen >= 0 and xloc + 1 - WordLen >= 0:
                c = 0
                ULSrch = "" 
                while c < WordLen:
                    ULSrch = ULSrch + listofstrings[yloc - c][xloc - c]
                    if len(ULSrch) == WordLen and WordList.check(ULSrch):
                        print(ULSrch, "located at x:",xloc + 1,"y:",yloc + 1, "going up and left!")
                        FoundWords += 1
                    c += 1
            if yloc + WordLen <= ydim and xloc + 1 - WordLen >= 0:
                c = 0
                DLSrch = ""
                while c < WordLen:
                    DLSrch = DLSrch + listofstrings[yloc + c][xloc - c]
                    if len(DLSrch) == WordLen and WordList.check(DLSrch):
                        print(DLSrch, "located at x:",xloc + 1,"y:",yloc + 1, "going up and right!")
                        FoundWords += 1
                    c += 1
            if yloc + 1 - WordLen >= 0 and xloc + WordLen <= xdim:
                c = 0
                URSrch = ""
                while c < WordLen:
                    URSrch = URSrch + listofstrings[yloc - c][xloc + c]
                    if len(URSrch) == WordLen and WordList.check(URSrch):
                        print(URSrch, "located at x:",xloc + 1,"y:",yloc + 1, "going down and left!")
                        FoundWords += 1
                    c += 1
print("Found", FoundWords, "total english words longer than", MinLength)                    
print("Note that coordinate x: 1, y: 1 is the top left corner")
##if len(WordList) == len(FoundWords):
##    print("All words located!")
##else:
##    print(len(WordList) - len(FoundWords),"Words not found, They are:")
##    for word in WordList:
##        if word not in FoundWords:
##            print(word)