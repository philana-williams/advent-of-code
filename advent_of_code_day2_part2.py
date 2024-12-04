import time
def readFile(fileName="input.txt"):
    fileObj = open(fileName)
    fileLineList = []

    for line in fileObj:
        cleanLine = line.strip()
        lineTuple = tuple(int(num) for num in cleanLine.split(" "))
        fileLineList.append(lineTuple)

    return fileLineList


def determineSafe(integerTuple):
    safeBool = True  # assume number will be safe
    # safe means:
    # 1 . all levels are decreasing or decreasing
    # 2 . min distance between numbers is 1, max distance between consecutive numbers are 3

    changeDict = {"increase": [], "decrease": [], "no change": []}
    numDistanceDict = dict()

    for currIndex in range(len(integerTuple) - 1):
        currNumber = integerTuple[currIndex]

        nextIndex = currIndex + 1
        nextNumber = integerTuple[nextIndex]

        numDistance = abs(currNumber - nextNumber)
        numDistanceDict[(currIndex, nextIndex)] = numDistance

        if currNumber == nextNumber:
            changeDict["no change"].append((currIndex, nextIndex))
        elif currNumber < nextNumber:
            changeDict["increase"].append((currIndex, nextIndex))
        else:  # currNumber > nextNumber
            changeDict["decrease"].append((currIndex, nextIndex))

    # print("changeDict: ", changeDict)
    # print("numDistanceDict: ", numDistanceDict)
    unsafeBoolDict = {"invalid maxDistance": [], "invalid no change": []}

    # unsafe reasons
    # minDistance in less than 1 (i.e. 0)
    # maxDistance is greater than 3
    # len 'no change' is greater than 0
    # len 'increase' is greater than 0 and so is len 'decrease'

    # check for unsafe distances
    for currIndex, nextIndex in numDistanceDict:
        numDistance = numDistanceDict[(currIndex, nextIndex)]

        if numDistance == 0:
            unsafeBoolDict["invalid no change"].append((currIndex, nextIndex))
        elif numDistance > 3:
            unsafeBoolDict["invalid maxDistance"].append((currIndex, nextIndex))

    # check for unsafe increase/decrease

    increaseIndices = changeDict["increase"]
    decreaseIndices = changeDict["decrease"]

    if (len(increaseIndices) >= len(decreaseIndices)) and len(decreaseIndices) != 0:
        unsafeBoolDict["invalid decrease"] = decreaseIndices

    if len(decreaseIndices) >= len(increaseIndices) and len(increaseIndices) != 0:
        unsafeBoolDict["invalid increase"] = increaseIndices

    unsafeIndicesSet = set()

    for reason in unsafeBoolDict:
        unsafeIndices = unsafeBoolDict[reason]
        for indices in unsafeIndices:
            unsafeIndicesSet.add(indices)

    return unsafeIndicesSet, unsafeBoolDict


def countSafe(fileLineList):
    safeCtn = 0
    # safeLineDict = dict()

    lineNumber = 0
    for line in fileLineList:
        unsafeIndicesSet, unsafeBoolDict = determineSafe(line)
        if len(unsafeIndicesSet) == 0:
            safeCtn += 1
            # safeLineDict[lineNumber]=line
            # print("{}: {}".format(lineNumber, line))

        else:
            index = 0
            while index < len(line) and len(unsafeIndicesSet) > 0:
                newLine = tuple(line[i] for i in range(len(line)) if i != index)
                unsafeIndicesSet, unsafeBoolDict = determineSafe(newLine)
                if len(unsafeIndicesSet) == 0:
                    safeCtn += 1
                    # print("{}: {}".format(lineNumber, line))
                else:
                    index += 1
        lineNumber += 1

    return safeCtn


def countSafeV2(fileLineList):
    safeCtn = 0

    lineNumber = 0
    for line in fileLineList:
        unsafeIndicesSet, unsafeBoolDict = determineSafe(line)
        # print("Line 0: {} \t Unsafe Indices: {} \t Unsafe Reasons: {}".format(line, unsafeIndicesSet, unsafeBoolDict))
        if len(unsafeIndicesSet) == 0:
            safeCtn += 1

            # print("{}: {}".format(lineNumber, line))


        elif len(unsafeIndicesSet) < 3:
            # print("entering elif")
            unsafeTupleSet = set()

            for reason in unsafeBoolDict:
                # print(reason)
                unsafeIndices = unsafeBoolDict[reason]
                # print(unsafeIndices)
                for unsafeTuple in unsafeIndices:
                    # print(unsafeTuple)
                    unsafeTupleSet.add(unsafeTuple)
            # print(unsafeTupleSet)

            unsafeTupleList = list(unsafeTupleSet)

            index = 0
            while index < len(unsafeTupleList) and len(unsafeIndicesSet) > 0:
                unsafeCurrIndex, unsafeNextIndex = unsafeTupleList[index]

                newLine = tuple(line[i] for i in range(len(line)) if i != unsafeCurrIndex)
                unsafeIndicesSet, unsafeBoolDict = determineSafe(newLine)
                # print("Line 1: {} \t Unsafe Indices 1: {} \t Unsafe Reasons: {}".format(newLine, unsafeIndicesSet,
                #                                                                         unsafeBoolDict))

                if len(unsafeIndicesSet) == 0:
                    safeCtn += 1

                else:
                    newLine = tuple(line[i] for i in range(len(line)) if i != unsafeNextIndex)
                    unsafeIndicesSet, unsafeBoolDict = determineSafe(newLine)
                    # print("Line 2: {} \t Unsafe Indices 1: {} \t Unsafe Reasons: {}".format(newLine, unsafeIndicesSet,
                    #                                                                         unsafeBoolDict))

                    if len(unsafeIndicesSet) == 0:
                        safeCtn += 1

                index += 1

        lineNumber += 1

    return safeCtn


def main():
    print("Advent of Code - Day 2 Part 2! Let's own Mikey!")
    fileLineList = readFile("input.txt")

    safeCtn = countSafeV2(fileLineList)
    print("Safe Count: ", safeCtn)

main()