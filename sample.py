import sys, word_frequency, random

def randomSample(textMap):
    return random.choice(list(textMap.wordMap.keys()))

def weightedSample(textMap):
    r = random.uniform(0, sum(textMap.wordMap.values()))
    s = 0.0
    for key, weight in textMap.wordMap.items():
        s += weight
        if r < s: return key
    return key

def testWeightedSample(textMap):
    results = {}
    for x in range(10000):
        chosen = weightedSample(textMap)
        results[chosen] = results.get(chosen, 0) + 1
    print(results)

if __name__ == "__main__":
    args = sys.argv
    text = open(args[1]).read().split()

    textMap = word_frequency.HashMap(text)
    textMap.histogram()

    print(randomSample(textMap))
    print(weightedSample(textMap))
    print(testWeightedSample(textMap))
