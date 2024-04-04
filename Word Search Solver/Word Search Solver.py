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
DummyArray2 = ["a", "a", "q", "g"]
DummyArray3 = ["r", "a", "p", "g"]
DummyArrayofArrays.append(DummyArray1)
DummyArrayofArrays.append(DummyArray2)
DummyArrayofArrays.append(DummyArray3)
print(DummyArrayofArrays)
x = 0
y = 0
l = 0
ll = 0
## Get Possible lengths of words to search for
WordListLen = []
for Word in WordList:
    l = len(Word)
    if l not in WordListLen:
        WordListLen.append(l)
print(WordListLen)
for length in WordListLen:
## Forward horizontal search pattern
    for array in DummyArrayofArrays:
        l = len(array)
        x = 0
        for letters in array:
            if x + length <= l:
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
    for yval in range(len(array)): #establish incrementing y value
        l = len(DummyArrayofArrays) # x dimension of grid
        y = 0 # starting position
        for xval in range(l):  # establish incrementing x value
            if y + length <= l: # determine if the resultant string would extend past the edge of the grid
                SearchString = ""
                while y > length:
                    SearchString += DummyArrayofArrays[y + yval][xval]
                    y += 1
                print(SearchString)