##Starting with things i know how to do that won't require research
## First gather list of words that need to be found
WordList = []
NextWord =input('Enter word to be added to search list, enter "Done!", without the quotation marks when complete')
while NextWord != "Done!":
    WordList.append(NextWord)
    NextWord =input('Enter word to be added to search list, enter "Done!", without the quotation marks when complete')
print(WordList)
    