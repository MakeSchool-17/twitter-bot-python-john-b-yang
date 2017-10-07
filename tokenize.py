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

def correct_caps(word):
    if word.isupper() and word != "I":
        word = word.lower()
    elif word[0].isupper():
        word = word.lower().capitalize()
    else:
        word = word.lower()
    return word

def create_word_list(filename):
    corpus = open(filename, 'r')
    word_list = [correct_caps(word) for word in re.findall(r"[\w']+|[.,!?;]", corpus.read())]
    corpus.close()
    return word_list

if __name__ == '__main__':
    # Perform tokenization + word frequency analysis
    output_file_read = open('book_sample.txt', 'r')
    word_dict = tokenize_text(output_file_read.read())
    print(word_dict)
