# PURPOSE:
# 1. Use DiffBot API to extract, parse, and clean text from webpage
# 2. Push this output to book_sample.txt file

import sys, random, requests, re

# Sample URL: http://api.diffbot.com/v3/article?token=yourtokenhere&url=https://en.wikipedia.org/wiki/Twitterbot
DIFFBOT_API_URL = 'http://api.diffbot.com/v3/article'
DIFFBOT_DEV_TOKEN = '658d3b5b3aa5add15a550691bb28064c'
BOOK_URL = "https://archive.org/stream/TheChroniclesOfNarnia/The%20Chronicles%20of%20Narnia_djvu.txt"

# Book URL List:
# 1. Cyrano de Bergerac: http://emotional-literacy-education.com/classic-books-online-b/cdben10.htm
# 2. Wizard of Oz: http://www.gutenberg.org/files/55/55-h/55-h.htm
# 3. Lion Witch & Wardrobe: https://archive.org/stream/TheChroniclesOfNarnia/The%20Chronicles%20of%20Narnia_djvu.txt

def get_article(article_url):
    # Create request parameters for API call
    params = { 'token': DIFFBOT_DEV_TOKEN,
               'url': article_url,
               'discussion': 'false' }

    res = requests.get(DIFFBOT_API_URL, params)
    res_obj = res.json()['objects'][0]

    return res_obj['text']

def clean_article(article_text):
    unwanted_punc = list(r'*_"}{][$^&~`')
    cleaned_text = ''

    for line in article_text:
        curr_line = line.replace("\n", " ")
        adjusted_line = ''.join(ch for ch in curr_line if ch not in unwanted_punc)
        cleaned_text += adjusted_line

    return cleaned_text

if __name__ == '__main__':
    # Perform web page parsing w/ Diffbot + writing into book_sample.txt file
    output_file_write = open('book_sample.txt', 'w')
    # Replace BOOK_URL with sys.argv[1] to take URL as parameter
    output_file_write.write(clean_article(get_article(BOOK_URL)))
    print('Corpus saved to {}'.format(output_file_write.name))
