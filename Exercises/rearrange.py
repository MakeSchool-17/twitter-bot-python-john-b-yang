import sys, random

def rearrangeWords(lineArgs):
    value = ""
    while len(lineArgs) > 0:
        index = random.randint(0, len(lineArgs) - 1)
        value += lineArgs[index] + " "
        lineArgs.pop(index)
    return value

if __name__ == '__main__':
    print('Enter as many as words as you like, separated by commas')
    lineArgs = sys.argv
    lineArgs.pop(0) # Remove first item in list (argument name)
    print(rearrangeWords(lineArgs))
