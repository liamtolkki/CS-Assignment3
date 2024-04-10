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
def printMatrix(matrix, rows, cols):
    isNegative = matrix[0][0] < 0
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == None:
                if isNegative:
                    print(" ", end="") #extra pad to account for negative - sign
                print("X", end="")
            else:
                print(matrix[i][j], end="")
            print(" ", end="")
                
        print() #newline

def main():
    if len(sys.argv) != 2:
        print("make sure to include the file name of the input file!\n")
        sys.exit(1)
    inputFileName = sys.argv[1] # argv[1] contains the second argument (filename)
    fileNumber = getNumber(inputFileName)
    inputPath = "testing/" + inputFileName
    #initialize all values to be null
    string1 = None
    string2 = None
    insertDeleteCost = None
    matchCost = None
    mismatchCost = None
    with open(inputPath, "r") as infile:
        string1 = infile.readline().strip()
        string2 = infile.readline().strip()
        insertDeleteCost = int(infile.readline().strip())
        matchCost = int(infile.readline().strip())
        mismatchCost = int(infile.readline().strip())
        infile.close()
    #stringArray will hold the costs as it goes (2D array)
    nRows = len(string1)
    nCols = len(string2)

    stringArray = create_2d_array(nRows, nCols)
    #initialize the first row and column with matchCost O(M + N):
    for i in range(nCols):
        stringArray[0][i] = matchCost 
    for i in range(nRows):
        stringArray[i][0] = matchCost
    print("String1: \"" + string1 + "\"")
    print("String2: \"" + string2 + "\"")

    printMatrix(stringArray, nRows, nCols) #testing purposes
    
if __name__ == "__main__":
    main()