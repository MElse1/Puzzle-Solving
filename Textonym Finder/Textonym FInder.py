import enchant

## import dictionary
englishDict = enchant.Dict("en_US")
print("Enter the word you would like to find the textonyms for!")
## collect word input

while True:
    try:
        wordInput = input("please only enter letters into the prompt:")
        if wordInput.isalpha():
            break
        else:
            raise
    except:
        print("please try again!")
wordInput = wordInput.upper()
inputNumbers = ""
for letter in wordInput:
    if letter == "A" or letter == "B" or letter == "C":
        inputNumbers = inputNumbers + "2"
    elif letter == "D" or letter == "E" or letter == "F":
        inputNumbers = inputNumbers + "3"
    elif letter == "G" or letter == "H" or letter == "I":
        inputNumbers = inputNumbers + "4"
    elif letter == "J" or letter == "K" or letter == "L":
        inputNumbers = inputNumbers + "5"
    elif letter == "M" or letter == "N" or letter == "O":
        inputNumbers = inputNumbers + "6"
    elif letter == "P" or letter == "Q" or letter == "R" or letter == "S":
        inputNumbers = inputNumbers + "7"
    elif letter == "T" or letter == "U" or letter == "V":
        inputNumbers = inputNumbers + "8"
    elif letter == "W" or letter == "X" or letter == "Y" or letter == "Z":
        inputNumbers = inputNumbers + "9"
## for letter in wordInput add proper T9 value
## Assign empty lists for later use
wordBuilderList = []
appList = []
## convert input numbers into a list of lists to build words later
for number in str(inputNumbers):
    match number:
        case "2":
            appList =["A", "B", "C", "1"]
            wordBuilderList.append(appList)
        case "3":
            appList =["D", "E", "F", "1"]
            wordBuilderList.append(appList)
        case "4":
            appList =["G", "H", "I", "1"]
            wordBuilderList.append(appList)
        case "5":
            appList =["J", "K", "L", "1"]
            wordBuilderList.append(appList)
        case "6":
            appList =["M", "N", "O", "1"]
            wordBuilderList.append(appList)
        case "7":
            appList =["P", "Q", "R", "S"]
            wordBuilderList.append(appList)
        case "8":
            appList =["T", "U", "V", "1"]
            wordBuilderList.append(appList)
        case "9":
            appList =["W", "X", "Y", "Z"]
            wordBuilderList.append(appList)

permutationCount = 1
for list in wordBuilderList:
    permutationCount = permutationCount * len(list)
resultList = []
for working in range(permutationCount):
    resultList.append(wordBuilderList[0][working % 4])
c = 0
resultList.sort()
for list in wordBuilderList:
    i = 0
    if c != 0:
        for working in range(permutationCount):
            resultList[i] = resultList[i] + list[working % 4]
            i += 1
    resultList.sort()
    c += 1
found = 0
for result in resultList:
    if "1" not in result and englishDict.check(result) and result != wordInput:
        print(result, "is a textonym of", wordInput)
        found += 1
if found == 0:
    print("There are no textonyms of",wordInput, "in this dictionary at least")
else:
    print("Found", found, "textonyms of", wordInput)

