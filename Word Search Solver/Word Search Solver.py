##Starting with things i know how to do that won't require research
## First gather list of words that need to be found
WordList = []
NextWord =input('Enter word to be added to search list, enter "Done!", without the quotation marks when complete')
while NextWord != "Done!":
    NextWord =input('Enter word to be added to search list, enter "Done!", without the quotation marks when complete')
    WordList.append(NextWord)
## Add conditional logic to remove "Done!" to the end of wordlist
    if NextWord == "Done!":
        WordList.remove("Done!")
print(WordList)
    