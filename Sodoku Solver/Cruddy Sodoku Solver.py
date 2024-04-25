import random
from re import match
from copy import deepcopy

## gather user grid
print("Please input the 9 rows of your sodoku puzzle in the following format:")
print("if your first line has a 7 in the 5th position type in 00007, or 000070000, the trailing 0's are not required.")
print("if you randomly input numbers that would make the puzzle unsolvable, the script will attempt to run 50000 times before it quits")
gather = 0
while gather == 0:
    try:
        userGrid = []
        for userInput in range(9):
            lineInput = str(input(f'Line {userInput + 1}:'))
            if len(lineInput) > 9:
                raise ValueError
            while len(lineInput) < 9:
                lineInput += "0"
            userLine = []
            for number in lineInput:
                if match("[0-9]", number):
                    userLine.append(number)
                else:
                    raise TypeError
            userGrid.append(userLine)
        gather = 1
    except ValueError:
        print("To many characters recieved")            
    except TypeError:
        print("Invalid characters received")
## in progress
inputArray = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
attempt = 0
finished = 0
while attempt <= 49999 and finished == 0:
    try:    
## reset grid for testing
        finalGrid = []
        finalGrid = deepcopy(userGrid)
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
                    if str(number) not in finalGrid[yloc] and str(number) not in yLine and str(number) not in threexThree and finalGrid[yloc][xloc] == "0":
                        finalGrid[yloc][xloc] = str(number)
                        placed += 1
                        break
        for line in finalGrid:
            for number in line:
                if number == "0":
                    finished = 0
                    raise 
                else:
                    finished = 1
    except:
        print("Placed", placed, "numbers before failure")
        print("Attempt number", attempt + 1, "failed, trying again.")
        attempt += 1
if finished == 1:
    print("Solution found!")
    for line in finalGrid:
        print(line)
else:
    print("No match found, are you sure you entered the numbers correctly?")