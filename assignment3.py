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
    print("\t", end="")
    for i in range(nCols - 1):
        print(string2[i] + "\t",end="")
    print()
    for i in range(nRows):
        if i > 0:
            print(string1[i - 1] + " ", end="")
        else:
            print("  ", end="")
        for j in range(nCols):
            if costMatrix[i][j] == None:
                print("X", end="")
            else:
                print(costMatrix[i][j], end="")
            print("\t", end="")
                
        print() #newline

#returns the cost of diagonal traversal
def alpha(i, j):
    #print("i: " + str(i) + "    j: " + str(j))
    if string1[i - 1] == string2[j - 1]:
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
    nRows = len(string1) + 1
    nCols = len(string2) + 1
    #costMatrix will hold the costs as it goes (2D array)
    costMatrix = create_2d_array(nRows, nCols)
    #initialize the first row and column with gapCost * i O(M + N):
    for i in range(nCols):
        costMatrix[0][i] = insertDeleteCost * i 
    for i in range(nRows):
        costMatrix[i][0] = insertDeleteCost * i
    #print("String1: \"" + string1 + "\"")
    #print("String2: \"" + string2 + "\"")

    #calculate the cell costs:
    #start with indexes at 1 since first row and column already filled out!
    for i in range(1, nRows):
        for j in range(1, nCols):
            diagonalCost = alpha(i, j) + costMatrix[i - 1][j - 1]
            gapDown = insertDeleteCost + costMatrix[i - 1][j]
            gapRight = insertDeleteCost + costMatrix[i][j - 1]
            #minimum cost becomes the cell
            costMatrix[i][j] = min(diagonalCost, gapDown, gapRight)
    #printMatrix() #testing purposes
    #the bottom right value is always the minimum cost of alignment
    minimumCost = 0 # = costMatrix[nRows - 1][nCols - 1] 
    #print("Minimum Cost: " + str(minimumCost))
    #traverse backwards:
    string1Aligned = [] #list of chars to be soon reversed and turned into a string
    string2Aligned = [] #same thing
    i = nRows - 1
    j = nCols - 1
    while i > 0 and j > 0: #until it reaches top left
        #find lowest adjacent cell:
        left = float('inf') #gets overwritten if not out of bounds
        up = float('inf')
        diagonal = float('inf')
        if j > 0:
            left = costMatrix[i][j - 1]
        if i > 0:
            up = costMatrix[i - 1][j]
        if i > 0 and j > 0:
            diagonal = costMatrix[i - 1][j - 1]
        minSelect = min(up, left, diagonal)
        if minSelect == left:
            #gap in string1
            #print("i = " + str(i) + "   j = " + str(j) + "\tLEFT")

            string2Aligned.append(string2[j - 1])
            string1Aligned.append('_')
            j = j - 1
            minimumCost += insertDeleteCost #pay the gap cost
        elif minSelect == up:
            #gap in string2
            #print("i = " + str(i) + "   j = " + str(j) + "\tUP")

            string1Aligned.append(string1[i - 1])
            string2Aligned.append('_')
            i = i - 1
            minimumCost += insertDeleteCost #pay the gap cost

        else:
            #diagonal
            #print("i = " + str(i) + "   j = " + str(j) + "\tDiag")
            string1Aligned.append(string1[i - 1])
            string2Aligned.append(string2[j - 1])
            minimumCost += alpha(i, j)
            i = i - 1
            j = j - 1
    #process character arrays:
    #they need to be reversed and then joined
    i = 0
    end = len(string1Aligned) - 1
    while i <= end:
        temp = string1Aligned[i]
        string1Aligned[i] = string1Aligned[end]
        string1Aligned[end] = temp
        i = i + 1
        end = end - 1
    i = 0
    end = len(string2Aligned) - 1
    while i <= end:
        temp = string2Aligned[i]
        string2Aligned[i] = string2Aligned[end]
        string2Aligned[end] = temp
        i = i + 1
        end = end - 1
    string1Aligned = "".join(string1Aligned)
    string2Aligned = "".join(string2Aligned)
    #print("String1 Aligned: \"" + string1Aligned + "\"")
    #print("String2 Aligned: \"" + string2Aligned + "\"")
    path = "testing/"
    file = "output.txt"
    if fileNumber > 0:
        file = "output" + str(fileNumber) + ".txt"
    outPath = path + file
    with open(outPath, "w") as outFile:
        outFile.write(str(minimumCost) + "\n")
        outFile.write(string1Aligned + "\n")
        outFile.write(string2Aligned + "\n")
        outFile.close()
    
if __name__ == "__main__":
    main()