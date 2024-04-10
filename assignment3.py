#Assignment 3
#String Matching
#Group: Liam Tolkkinen
#due 04/11/2024

import re
import sys

def create_2d_array(rows, cols):
    return [[None for _ in range(cols)] for _ in range(rows)]
# Returns a number found in the filename
def getNumber(filename):
    digits = re.findall(r'\d+', filename) # Regex to find the digits in the name
    if not digits:
        return 0
    number = int(''.join(digits)) #concatenate the digits together and cast to int
    return number
def printMatrix():
    isNegative = costMatrix[0][0] < 0
    for i in range(nRows):
        for j in range(nCols):
            if costMatrix[i][j] == None:
                #if isNegative:
                #    print(" ", end="") #extra pad to account for negative - sign
                print("X", end="")
            else:
                print(costMatrix[i][j], end="")
            print("\t", end="")
                
        print() #newline

#returns the cost of diagonal traversal
def alpha(i, j):
    if string1[i] == string2[j]:
        return matchCost
    else:
        return mismatchCost



def main():
    if len(sys.argv) != 2:
        print("make sure to include the file name of the input file!\n")
        sys.exit(1)
    inputFileName = sys.argv[1] # argv[1] contains the second argument (filename)
    fileNumber = getNumber(inputFileName)
    inputPath = "testing/" + inputFileName
    #declare all global variables
    global string1
    global string2
    global insertDeleteCost
    global matchCost
    global mismatchCost
    global nRows
    global nCols
    global costMatrix 

    with open(inputPath, "r") as infile:
        string1 = infile.readline().strip()
        string2 = infile.readline().strip()
        insertDeleteCost = int(infile.readline().strip())
        matchCost = int(infile.readline().strip())
        mismatchCost = int(infile.readline().strip())
        infile.close()
    #initialize values
    nRows = len(string1)
    nCols = len(string2)
    #costMatrix will hold the costs as it goes (2D array)
    costMatrix = create_2d_array(nRows, nCols)
    #initialize the first row and column with gapCost * i O(M + N):
    for i in range(nCols):
        costMatrix[0][i] = insertDeleteCost * i 
    for i in range(nRows):
        costMatrix[i][0] = insertDeleteCost * i
    print("String1: \"" + string1 + "\"")
    print("String2: \"" + string2 + "\"")

    #calculate the cell costs:
    #start with indexes at 1 since first row and column already filled out!
    for i in range(1, nRows):
        for j in range(1, nCols):
            diagonalCost = alpha(i, j) + costMatrix[i - 1][j - 1]
            gapDown = insertDeleteCost + costMatrix[i - 1][j]
            gapRight = insertDeleteCost + costMatrix[i][j - 1]
            #minimum cost becomes the cell
            costMatrix[i][j] = min(diagonalCost, gapDown, gapRight)


    printMatrix() #testing purposes


    
if __name__ == "__main__":
    main()