import sys, random, requests, re
from path import path

def randomWords(num_of_words):
    # words = path("/usr/share/dict/words").bytes() # Returns raw byte form of file contents, so new lines -> \n
    words = open("/usr/share/dict/words").read().splitlines()
    output = ""
    while (num_of_words > 0):
        randIndex = random.randint(0, len(words)-1)
        output += words[randIndex] + " "
        num_of_words -= 1;
    print(output)

def vocabGame():
    words = open("/usr/share/dict/words").read().splitlines()
    randWord = words[random.randint(0, len(words)-1)]
    print("What does this word mean?: " + randWord)
    findDef(randWord)

def findDef(word):
    site = requests.get("http://dictionary.reference.com/browse/"+str(word)+"?s=t").text
    items = re.findall('<div class="def-content">\s.*?</div>', site, re.S)
    definitions = [re.sub('<.*?>', '', item).strip() for item in items]

    count = 1
    for meaning in definitions:
        print(str(count) + ". " + meaning)
        count += 1

if __name__ == "__main__":
    lineArgs = sys.argv
    lineArgs.pop(0)
    # randomWords(int(lineArgs[0]))
    vocabGame()
