# Module Concept
# - Run file independently as script
# - Can be imported by other files

import random

quotes = ("Real Stupidity beats Artifical Intelligence every time",
          "How much wood could a woodchuck chuck if a woodchuck could chuck wood",
          "Stay in yo lane")

def random_python_quote():
    rand_index = random.randint(0, len(quotes) - 1)
    return quotes[rand_index]

# Executable Section
if __name__ == '__main__':
    print(random_python_quote())
