import re

def countWords(filename):
    words = []
    openFile = open(filename, 'r')
    wordList = openFile.read()
    wordList2 = re.findall(r"[a-zA-Z]+", wordList)
    #print(wordList)
    for line in wordList2:
        words.append(line.lower())

    counts = dict()
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    with open("test.txt", 'w') as f:
        for elem in sorted(counts.items()):
            f.write(elem[0] + ' ' +  str(elem[1]) + '\n')
    print("written to file!")
def main():
    countWords("declaration.txt")


if __name__ == '__main__':
    main()