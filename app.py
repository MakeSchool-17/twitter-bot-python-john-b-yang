import generate_corpus, tokenize

BOOK_URL = "https://archive.org/stream/TheChroniclesOfNarnia/The%20Chronicles%20of%20Narnia_djvu.txt"

if __name__ == '__main__':
    # 1. Generate text file of corpus source
    output_file_write = open('book_sample.txt', 'w')

    raw_text = generate_corpus.get_article(BOOK_URL)
    clean_text = generate_corpus.clean_article(raw_text)

    output_file_write.write(clean_text)
    print('Corpus saved to {}'.format(output_file_write.name))

    # 2. Generate dictionary for word analysis of corpus text
    output_file_read = open('book_sample.txt', 'r')
    word_list = tokenize.create_word_list(output_file_read.read())
    word_dict = tokenize.tokenize_text(output_file_read.read())

    # 3. Create Markov Chain Representation of corpus from word_list
    # then perform random walk for sentence generation
