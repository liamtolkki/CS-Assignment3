import random as rand
import math

def weighted_random(start_index, size, max_distance):
    weights = [math.exp(-((i - start_index) ** 2) / (2 * (max_distance ** 2))) for i in range(size)]
    total_weight = sum(weights)
    normalized_weights = [w / total_weight for w in weights]
    return rand.choices(range(size), weights=normalized_weights)[0]

def main():
    dictionary = []
    with open("cleanDictionary.txt", "r") as dictionaryFile:
        word = dictionaryFile.readline().strip()
        while (word):
            word = dictionaryFile.readline().strip()
            dictionary.append(word)
        dictionaryFile.close()
    nFiles = 1 #default (override if ran in automatic mode)
    auto = str(input("Run generator automatically? (y/n) "))
    firstFileNumber = 0 #default
    outFile = ""
    allowNegativeCostMatch = False
    costMatch = str(input("Allow negative cost for letter match? (y/n) "))
    if costMatch.lower() == "y":
        allowNegativeCostMatch = True
    if auto.lower() == "y":
        nFiles = int(input("How many files? "))
        firstFileNumber = int(input("Starting file number? "))
    else:
        outFile = str(input("Name of file? (Ex: \"input3.txt\") "))

    for i in range(nFiles): #do for every file
        
        if auto.lower() == "y":
            if firstFileNumber == 0:
                outFile = "input.txt"
            else:
                outFile = "input" + str(firstFileNumber) + ".txt"
            firstFileNumber += 1 #increment
            
        wordIndex = rand.randint(0, len(dictionary) - 1)
        randWord1 = dictionary[wordIndex] #get 1st random word

        #2nd random word, very close to the first one, for matching purposes
        randWord2 = dictionary[wordIndex + weighted_random(100, len(dictionary) - wordIndex - 1, (len(dictionary) - wordIndex - 1) / 20)] 
        insertDeleteCost = rand.randint(1, 4)
        matchCost = rand.randint(0, 2)
        letterChangeCost = rand.randint(1,4)
        if allowNegativeCostMatch:
            matchCost = rand.randint(-2, 2)
            test = rand.randint(0,1)
            if test == 0:
                matchCost = 0
        dif = matchCost - insertDeleteCost
        if dif >= 0:
            insertDeleteCost = (insertDeleteCost + dif) + 1 #make sure that match cost is LOWER than mismatch!
        dif = matchCost - letterChangeCost
        if dif >= 0:
            letterChangeCost = (letterChangeCost + dif) + 1 #make sure that match cost is LOWER than letter change cost!
        #output to file:
        path = "../testing/" + outFile
        with open(path, "w") as file:
            file.write(randWord1 + "\n")
            file.write(randWord2 + "\n")
            file.write(str(insertDeleteCost) + "\n")
            file.write(str(matchCost) + "\n")
            file.write(str(letterChangeCost))

            file.close()

        

    








if __name__ == "__main__":
    main()