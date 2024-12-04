import numpy as np


def readFile(fileName="input.txt"):
    fileObj = open(fileName)
    lineList = []
    for line in fileObj:
        lineList.append(line.strip())

    return lineList


def aLocator(lineList):
    aLocationList = []

    for lineIndex in range(len(lineList)):
        line = lineList[lineIndex]
        for characterIndex in range(len(line)):
            character = line[characterIndex]
            if character.lower() == "a":
                aLocationList.append((lineIndex, characterIndex))
    return aLocationList


def aMatrixBuilder(lineList):
    aLocationList = aLocator(lineList)
    aMatrix = []

    for lineNumber, characterIndex in aLocationList:
        upperLineNumber = lineNumber - 1
        lowerLineNumber = lineNumber + 1
        rightAdjacentIndex = characterIndex + 1
        leftAdjacentIndex = characterIndex - 1

        # make sure we don't run into index errors
        if (upperLineNumber != -1 and leftAdjacentIndex != -1) and (
                lowerLineNumber < len(lineList) and rightAdjacentIndex < len(lineList[0])):
            aGrid = []
            upperStr = lineList[upperLineNumber][leftAdjacentIndex:rightAdjacentIndex + 1]
            aGrid.append(upperStr)

            middleStr = lineList[lineNumber][leftAdjacentIndex:rightAdjacentIndex + 1]
            aGrid.append(middleStr)

            lowerStr = lineList[lowerLineNumber][leftAdjacentIndex:rightAdjacentIndex + 1]
            aGrid.append(lowerStr)

            aMatrix.append(aGrid)

    return aMatrix


def transposeXMASDiagonal(aGrid):
    diagList = []
    matrix = np.array([list(line) for line in aGrid])

    diagonals = [matrix[::-1, :].diagonal(i) for i in range(-matrix.shape[0] + 1, matrix.shape[1])]
    diagonals.extend(matrix.diagonal(i) for i in range(matrix.shape[1] - 1, -matrix.shape[0], -1))

    for diag in diagonals:
        if len(diag) == 3:
            diagList.append("".join(diag))

    return diagList


def countXMASInList(lineList):
    xmasCtn = 0
    for line in lineList:
        if line in ("SAM", "MAS"):
            xmasCtn += 1
    return xmasCtn


def countAllX_MAS(lineList):
    xmasCtn = 0
    aMatrices = aMatrixBuilder(lineList)

    for aGrid in aMatrices:
        diagonalLineList = transposeXMASDiagonal(aGrid)
        aGridCtn = countXMASInList(diagonalLineList)
        if aGridCtn == 2:
            xmasCtn += 1
    return xmasCtn


def main():
    print("Advent of Code - Day 4 - Part 1! Let's own Mikey!")
    lineList = readFile("input.txt")
    X_MASCtn = countAllX_MAS(lineList)
    print("X-MAS Count: ", X_MASCtn)


main()
