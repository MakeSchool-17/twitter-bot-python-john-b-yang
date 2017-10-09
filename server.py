from flask import Flask
import make_sentence
app = Flask(__name__)

@app.route('/')
def hello_world():
    return make_sentence.run()

if __name__ == '__main__':
    app.run()
