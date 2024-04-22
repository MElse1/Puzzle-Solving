import random
## in progress
inputArray = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
finished = 0
attempt = 0
while finished == 0:
    try:    
## reset grid for testing
        finalGrid = []
        for line in range(9):
            insertLine = []
            for number in range(9):
                insertLine.append("")
            finalGrid.append(insertLine)
## reset placed variable
        placed = 0
## iterate through grid
        for yloc in range(9):
            for xloc in range(9):
## initialze arrays to gather contents of vertical lines and the 3 x 3 subgrids of the grid
                yLine = []
                threexThree = []
## generate contents of Y line
                for number in range(9):
                    yLine.append(finalGrid[number][xloc])
## generate contents of 3x3 subgrid
                ySubGrid = ((((yloc) // 3) * 3))
                xSubGrid = ((((xloc) // 3) * 3))
                for ySubLoc in range(3):
                    for xSubLoc in range(3):
                        threexThree.append(finalGrid[ySubGrid + ySubLoc][xSubGrid + xSubLoc])
                random.shuffle(inputArray)
                for number in inputArray:
                    if str(number) not in finalGrid[yloc] and str(number) not in yLine and str(number) not in threexThree:
                        finalGrid[yloc][xloc] = str(number)
                        placed += 1
                        break
        for line in finalGrid:
            for number in line:
                if number == "":
                    finished = 0
                    raise
                else:
                    finished = 1
    except:
        print("Placed", placed, "numbers before failure")
        print("Random attempt number", attempt, "failed, trying again.")
        attempt += 1
for line in finalGrid:
    print(line)