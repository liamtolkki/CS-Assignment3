#Assignment 3
#Group: Liam Tolkkinen
#due 04/11/2024

import re
import sys

# Returns a number found in the filename
def getNumber(filename):
    digits = re.findall(r'\d+', filename) # Regex to find the digits in the name
    if not digits:
        return 0
    number = int(''.join(digits)) #concatenate the digits together and cast to int
    return number

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
        string1 = infile.readline()
        string2 = infile.readline()
        insertDeleteCost = int(infile.readline().strip())
        matchCost = int(infile.readline().strip())
        mismatchCost = int(infile.readline().strip())
        infile.close()

if __name__ == "__main__":
    main()