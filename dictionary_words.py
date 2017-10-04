import sys, random
from path import path

def randomWords(num_of_words):
    # words = path("/usr/share/dict/words").bytes() # Returns raw byte form of file contents, so new lines -> \n
    words = open("/usr/share/dict/words").read().splitlines()
    output = ""
    while (num_of_words > 0):
        randIndex = random.randint(0, len(words)-1)
        output += words[randIndex] + " "
        num_of_words -= 1;
    return output


if __name__ == "__main__":
    lineArgs = sys.argv
    lineArgs.pop(0)
    print(randomWords(int(lineArgs[0])))
