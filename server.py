from flask import Flask
import make_sentence
app = Flask(__name__)

MARKOV_GRAM_LENGTH = 5

@app.route('/')
def hello_world():
    return make_sentence.run()

if __name__ == '__main__':
    app.run()
