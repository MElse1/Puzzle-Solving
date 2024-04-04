## Starting with things i know how to do that won't require research
## First gather list of words that need to be found
WordList = []
NextWord =input('Enter word to be added to search list, enter "Done!", without the quotation marks when complete:')
while NextWord != "Done!":
    WordList.append(NextWord)
    NextWord = input('Enter word to be added to search list, enter "Done!", without the quotation marks when complete:')
## Build a dummy array to test word finding logic
DummyArrayofArrays = []
DummyArray1 = ["c", "a", "p", "e"]
DummyArray2 = ["a", "a", "q", "g"]
DummyArray3 = ["r", "j", "p", "g"]
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
## Forward horizontal search pattern
for length in WordListLen:
    for array in DummyArrayofArrays:
        ll = 0
        l = len(array)
        c = 0
        for letters in array:
            if c + length <= l:
                ll = 0
                SearchString = ""
                while ll < length:
                    SearchString = SearchString + array[ll + c]
                    ll += 1
                print(SearchString)
                c + 1
        