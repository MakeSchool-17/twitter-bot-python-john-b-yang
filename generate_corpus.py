# PURPOSE:
# 1. Use DiffBot API to extract, parse, and clean text from webpage
# 2. Push this output to book_sample.txt file

import sys, random, requests, re

# Sample URL: http://api.diffbot.com/v3/article?token=yourtokenhere&url=https://en.wikipedia.org/wiki/Twitterbot
DIFFBOT_API_URL = 'http://api.diffbot.com/v3/article'
DIFFBOT_DEV_TOKEN = '658d3b5b3aa5add15a550691bb28064c'
BOOK_URL = "https://archive.org/stream/twentythousandle00verniala/twentythousandle00verniala_djvu.txt"

# Book URL List:
# * Word Counts Here: http://commonplacebook.com/art/books/word-count-for-famous-novels/
# 1. Cyrano de Bergerac: http://emotional-literacy-education.com/classic-books-online-b/cdben10.htm
# 2. Wizard of Oz: http://www.gutenberg.org/files/55/55-h/55-h.htm
# 3. Lion Witch & Wardrobe: https://archive.org/stream/TheChroniclesOfNarnia/The%20Chronicles%20of%20Narnia_djvu.txt (Works, book too long)
# 4. Dr. Dolittle: http://www.gutenberg.org/files/501/501-h/501-h.htm (Not working)
# 5. Alice in Wonderland: https://archive.org/stream/alicesadventures19033gut/19033.txt (Works okay, large blob of license text)
# 6. Animal Farm: http://gutenberg.net.au/ebooks01/0100011h.html (Works, too short)
# 7. Gulliver's Travels: http://www.gutenberg.org/files/829/829-h/829-h.htm

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
    output_file_write.close()
