import re
import numpy as np
def readFile(fileName="input.txt"):
    fileObj = open(fileName)
    lineList = []
    for line in fileObj:
        lineList.append(line.strip())

    return lineList


def countXMASInLine(line):
    countXMASInLine = 0
    XMASInLine = re.findall("XMAS",line)
    countXMASInLine += len(XMASInLine)

    reverseLine = line[::-1]
    XMASInReverseLine = re.findall("XMAS", reverseLine)
    countXMASInLine+= len(XMASInReverseLine)
    return countXMASInLine

def countXMASInList(lineList):
    xmasCtn = 0
    for line in lineList:
        xmasCtn += countXMASInLine(line)
    return xmasCtn

def transposeXMASVertical(lineList):
    transposeLineList = []

    for index in range(len(lineList[0])):
        transposeLineList.append("")

    for line in lineList:
        for index in range(len(line)):
            transposeLineList[index] += line[index]
    return transposeLineList

def transposeXMASDiagonal(lineList):
    diagList = []
    matrix = np.array([list(line) for line in lineList])

    diagonals = [matrix[::-1, :].diagonal(i) for i in range(-matrix.shape[0] + 1, matrix.shape[1])]
    diagonals.extend(matrix.diagonal(i) for i in range(matrix.shape[1] - 1, -matrix.shape[0], -1))

    for diag in diagonals:
        diagList.append("".join(diag))
    return diagList


def countAllXMAS(lineList):
    xmasCtn = 0
    verticalLineList = transposeXMASVertical(lineList)
    diagonalLineList = transposeXMASDiagonal(lineList)

    xmasCtn += (countXMASInList(lineList) + countXMASInList(verticalLineList) + countXMASInList(diagonalLineList))
    return xmasCtn


def main():
    print("Advent of Code - Day 4 - Part 1! Let's own Mikey!")
    lineList = readFile("input.txt")

    xmasCtn = countAllXMAS(lineList)

    print("XMAS Count: ",xmasCtn)

main()
