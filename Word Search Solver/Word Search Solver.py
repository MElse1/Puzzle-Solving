import OCR_Letter_Grid as OCG
## Starting with things i know how to do that won't require research
## First gather list of words that need to be found
WordList = []
NextWord =input('Enter word to be added to search list, enter "Done!", without the quotation marks when complete:')
while NextWord != "Done!":
    WordList.append(NextWord.lower())
    NextWord = input('Enter word to be added to search list, enter "Done!", without the quotation marks when complete:')
## Build a dummy array to test word finding logic
print("Enter the path to the picture of the letter grid")
print("The easiest way to do this is to right click the file and select 'Copy as Path'")
print("Make sure you remove the 's from the paste")
x = input()
DummyArrayofArrays = OCG.OCRLG(x)
print(DummyArrayofArrays)
x = 0
y = 0
l = 0
ll = 0
## Get Possible lengths of words to search for
WordListLen = []
for Word in WordList:
    l = len(Word)
    if l not in WordListLen: ## deduplicate list
        WordListLen.append(l)
for length in WordListLen:
## Forward horizontal search pattern
    for array in DummyArrayofArrays:
        l = len(array)
        x = 0
        for letters in array:
            if x + length <= l:
                print(x + length)
                print(l)
                c = 0
                SearchString = ""
                while c < length:
                    SearchString = SearchString + array[c + x]
                    c += 1
                if SearchString in WordList:
                    print(SearchString,"located at x:", x + 1, "y:", y + 1, "Going right")
                x += 1
        y += 1
    y = 0
## Reverse horizontal search pattern
    for array in DummyArrayofArrays:
        l = len(array)  # x dimension of grid (4)
        x = 0 # starting position
        for letters in array: # iterate through each letter in array
            if x + length <= l: # starting position + search length needs to be less than array length
                c = -1 # iteration variable per search string, start with end of string
                SearchString = "" # search string variable duh
                while abs(c + 1) < length: # build search string to length of words to be searched for
                    SearchString = SearchString + array[c - x] # see above
                    c -= 1 # searching backwards so the iteration variable needs to de-increment instead of increment
                if SearchString in WordList:
                    print(SearchString,"located at x:", l - x, "y:", y + 1, "Going Left")
                x += 1
        y += 1
## forward vertical search pattern
    x = 0
    y = 0
    l = len(DummyArrayofArrays) # y dimension of grid
    for yval in range(len(array)): #establish incrementing y value
        for xval in range(l):  # establish incrementing x value
            if yval + length <= l: # determine if the resultant string would extend past the edge of the grid
                SearchString = ""
                c = 0
                while c < length:
                    SearchString = SearchString + str(DummyArrayofArrays[c + yval][xval])
                    c += 1
                    if SearchString in WordList and len(SearchString) == length:
                        print(SearchString,"located at x:", xval + 1,"y:", yval + 1,"Going Down")
## reverse vertical search pattern
    for yval in range(len(array)): #establish incrementing y value
        for xval in range(l):  # establish incrementing x value
            if yval + length <= l: # determine if the resultant string would extend past the edge of the grid
                SearchString = ""
                c = -1
                while abs(c + 1) < length:
                    SearchString = SearchString + str(DummyArrayofArrays[c - yval][xval])
                    c -= 1
                    if SearchString in WordList and len(SearchString) == length:
                        print(SearchString,"located at x:", xval + 1,"y:", l - yval,"Going Up")
## up left search pattern
    for yval in range(len(array)): #establish incrementing y value
        for xval in range(l):  # establish incrementing x value
            if yval + length <= l and xval + length <= l: # determine if the resultant string would extend past the edge of the grid
                SearchString = ""
                c = -1
                while abs(c + 1) < length:
                    SearchString = SearchString + str(DummyArrayofArrays[c - yval][c - xval])
                    c -= 1
                    if SearchString in WordList and len(SearchString) == length:
                        print(SearchString,"located at x:",l - xval,"y:", l - yval,"Going Up and Left")
## down right search pattern    
    for yval in range(len(array)): #establish incrementing y value
        for xval in range(l):  # establish incrementing x value
            if yval + length <= l and xval + length <= l: # determine if the resultant string would extend past the edge of the grid
                SearchString = ""
                c = 0
                while c < length:
                    SearchString = SearchString + str(DummyArrayofArrays[c + yval][c + xval])
                    c += 1
                    if SearchString in WordList and len(SearchString) == length:
                        print(SearchString,"located at x:", xval + 1,"y:", yval + 1,"Going Down and Right")
## up right search pattern
    for yval in range(len(array)): #establish incrementing y value
        for xval in range(l):  # establish incrementing x value
            if yval + length <= l and xval + length <= l: # determine if the resultant string would extend past the edge of the grid
                SearchString = ""
                c = -1
                d = 0
                while abs(c + 1) < length:
                    SearchString = SearchString + str(DummyArrayofArrays[c - yval][d + xval])
                    c -= 1
                    d += 1
                    if SearchString in WordList and len(SearchString) == length:
                        print(SearchString,"located at x:",l - xval,"y:", l - yval,"Going Up and Right")
## down left search pattern
    for yval in range(len(array)): #establish incrementing y value
        for xval in range(l):  # establish incrementing x value
            if yval + length <= l and xval + length <= l: # determine if the resultant string would extend past the edge of the grid
                SearchString = ""
                c = 0
                d = -1
                while abs(d + 1) < length:
                    SearchString = SearchString + str(DummyArrayofArrays[c + yval][d - xval])
                    c += 1
                    d -= 1
                    if SearchString in WordList and len(SearchString) == length:
                        print(SearchString,"located at x:",l - xval,"y:", l - yval,"Going Down and Right")                        