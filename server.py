from flask import Flask
import make_sentence
import os
app = Flask(__name__)

@app.route('/')
def hello_world():
    return make_sentence.run()

if __name__ == '__main__':

    # Required for Heroku's port attachment during deployment
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
