# PURPOSE:
# 1. Tokenize contents of book_sample.txt
# 2. Perform frequency analysis on word appearances

import sys, random, requests, re

def tokenize_text(article_text):
    split_text = article_text.split()
    token_dict = {}

    for word in split_text:
        word = remove_punctuation(word).lower()
        if word in token_dict:
            token_dict[word] += 1
        else:
            token_dict[word] = 1

    if '' in token_dict:
        del token_dict['']

    return token_dict

def remove_punctuation(text):
    no_punc_text = re.sub('[,.()]', '', text)
    no_punc_text = re.sub('--', ' ', no_punc_text)
    return no_punc_text

if __name__ == '__main__':
    # Perform tokenization + word frequency analysis
    output_file_read = open('book_sample.txt', 'r')
    word_dict = tokenize_text(output_file_read.read())
    print(word_dict)
