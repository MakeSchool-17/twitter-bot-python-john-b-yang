import sys, random, requests, re
from path import path

# Generates 'num_of_words' random words selected from system dictionary
def randomWords(num_of_words):
    # words = path("/usr/share/dict/words").bytes() # Returns raw byte form of file contents, so new lines -> \n
    words = open("/usr/share/dict/words").read().splitlines()
    output = ""
    while (num_of_words > 0):
        randIndex = random.randint(0, len(words)-1)
        output += words[randIndex] + " "
        num_of_words -= 1;
    print(output)

# Grabs random word from system dictionary, then calls findDef to generate definition
def vocabGame():
    words = open("/usr/share/dict/words").read().splitlines()
    randWord = words[random.randint(0, len(words)-1)]
    print("What does this word mean?: " + randWord)
    findDef(randWord)

# Given word, calls Dictionary.com web page, parses web content, and prints all definitions back
def findDef(word):
    site = requests.get("http://dictionary.reference.com/browse/"+str(word)+"?s=t").text
    items = re.findall('<div class="def-content">\s.*?</div>', site, re.S)
    definitions = [re.sub('<.*?>', '', item).strip() for item in items]

    count = 1
    for meaning in definitions:
        print(str(count) + ". " + meaning)
        count += 1

if __name__ == "__main__":
    user_input = input('Enter one number specifying number of random words you want: ')
    randomWords(int(user_input))
    vocabGame()
