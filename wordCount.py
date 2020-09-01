import re

def countWords(filename):
    words = []
    # open text file
    openFile = open(filename, 'r')
    wordList = openFile.read()
    # removes all characters other than alphabet characters
    wordList2 = re.findall(r"[a-zA-Z]+", wordList)

    # loop to switch all characters to lowercase and store each word to words list
    for line in wordList2:
        words.append(line.lower())

    # loop to count word occurences and store it in a dictionary
    counts = dict()
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    # writing output in the correct format to match key
    with open("myOutput.txt", 'w') as f:
        for elem in sorted(counts.items()):
            f.write(elem[0] + ' ' +  str(elem[1]) + '\n')
    print("written to file!")

def main():
    countWords("declaration.txt")

if __name__ == '__main__':
    main()