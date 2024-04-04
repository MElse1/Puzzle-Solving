##Starting with things i know how to do that won't require research
## First gather list of words that need to be found
WordList = []
NextWord =input('Enter word to be added to search list, enter "Done!", without the quotation marks when complete:')
while NextWord != "Done!":
    WordList.append(NextWord)
    NextWord = input('Enter word to be added to search list, enter "Done!", without the quotation marks when complete:')
## Build a dummy array to test word finding logic
DummyArrayofArrays = []
DummyArray1 = ["c", "a", "t"]
DummyArray2 = ["a", "a", "q"]
DummyArray3 = ["r", "j", "p"]
DummyArrayofArrays.append(DummyArray1)
DummyArrayofArrays.append(DummyArray2)
DummyArrayofArrays.append(DummyArray3)
print(DummyArrayofArrays)