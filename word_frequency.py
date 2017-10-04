import requests, string

class HashMap():

    book = ""
    wordMap = {}

    def __init__(self, text):
        self.book = text

    def histogram(self):
        # Build Hashmap
        for word in self.book:
            # Replace Punctuation
            for c in string.punctuation:
                word.replace(c, '')
            # If word in the map, iterate count
            if word in self.wordMap:
                self.wordMap[word] += 1
            else:
                self.wordMap[word] = 1

        return self.wordMap

    def unique_words(self):
        return len(self.histogram().keys())

    def frequency(self, word):
        return self.histogram().get(word)

    def getWordCount(self):
        return len(self.book)

    def printKeys(self):
        self.histogram()
        for x in self.wordMap:
            print(x)

    def __repr__(self):
        return str(self.wordMap)


if __name__ == '__main__':
    # Dr. Dolittle!
    book = requests.get("https://www.gutenberg.org/files/501/501-h/501-h.htm").text.split()
    bookMap = HashMap(book)
    print("Unique words: " + str(bookMap.unique_words()))
    print("Number of appearances for 'Dolittle': " + str(bookMap.frequency("Dolittle")))
