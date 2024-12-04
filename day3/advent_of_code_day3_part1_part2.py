import re

def readFile(fileName="input.txt"):
    fileObj = open(fileName)
    fileLine = ""
    for line in fileObj:
        cleanLine = line.strip()
        fileLine += cleanLine

    return fileLine

def parseInstructions(line):
    findPattern = re.search("don't\(\).*?do\(\)",line)
    while findPattern:
        line = re.sub("don't\(\).*?do\(\)","",line,count=1)
        findPattern = re.search("don't\(\).*?do\(\)", line)

    return re.sub("don't\(\).*","",line)



def findMatches(line):
    return re.findall("mul\((?<!\d)\d{1,3}(?!\d),(?<!\d)\d{1,3}(?!\d)\)",line)

def processMatchList(matchList):
    matchSum = 0
    for match in matchList:
        cleanMatch = match.replace("mul(","").replace(")","")
        firstNumStr, secondNumStr = cleanMatch.split(",")
        matchSum += int(firstNumStr) * int(secondNumStr)

    return matchSum

def computeMultiSumPart2(line):
    parsedLine = parseInstructions(line)
    patternMatches = findMatches(parsedLine)
    multiSum = processMatchList(patternMatches)
    return multiSum

def computeMultiSumPart1(line):
    patternMatches = findMatches(line)
    multiSum = processMatchList(patternMatches)
    return multiSum

def main():
    print("Advent of Code - Day 3! Let's own Mikey!")
    fileLine= readFile()

    multiSumPart1 = computeMultiSumPart1(fileLine)
    print("Multiplication Sum Part 1: {}".format(multiSumPart1))

    multiSumPart2 = computeMultiSumPart2(fileLine)
    print("Multiplication Sum Part 2: {}".format(multiSumPart2))



main()
