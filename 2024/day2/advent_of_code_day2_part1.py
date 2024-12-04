def readFile(fileName = "input.txt"):
    fileObj = open(fileName)
    fileLineList = []

    for line in fileObj:
        cleanLine = line.strip()
        lineTuple = tuple(int(num) for num in cleanLine.split(" "))
        fileLineList.append(lineTuple)

    return fileLineList


def determineSafe(integerTuple):

    safeBool = True # assume njumber will be safe
    # safe means:
        # 1 . all levels are decreasing or decreasing
        # 2 . min distance between numbers is 1, max distance between consecutive numbers are 3


    changeDict = {"increase":0,"decrease":0,"no change":0}
    maxChange = 0
    minChange = float('inf')

    for currIndex in range(len(integerTuple)-1):
        currNumber = integerTuple[currIndex]

        nextIndex = currIndex+1
        nextNumber = integerTuple[nextIndex]

        numDistance = abs(currNumber - nextNumber)

        if numDistance > maxChange:
            maxChange = numDistance

        if numDistance < minChange:
            minChange = numDistance

        if currNumber == nextNumber:
            changeDict["no change"]+=1
        elif currNumber < nextNumber:
            changeDict["increase"]+=1
        else: # currNumber > nextNumber
            changeDict["decrease"]+=1

    # change greater than 3 --> unsafe
    if maxChange > 3:
        safeBool = False
    # change less than 1 --> unsafe
    if minChange < 1:
        safeBool = False

    # no change --> unsafe
    if changeDict["no change"]>0:
        safeBool = False

    # increase and decrease in same list --> unsafe
    if changeDict["increase"]>0 and changeDict["decrease"]>0:
        safeBool = False

    return safeBool

def countSafe(fileLineList):
    safeCtn = 0

    for line in fileLineList:
        safeBool = determineSafe(line)
        if safeBool:
            safeCtn+=1
    return safeCtn












def main():
    print("Advent of Code - Day 2 Part 1! Let's own Mikey!")
    fileLineList = readFile()
    safeCtn = countSafe(fileLineList)
    print("Safe Count: ",safeCtn)


main()
