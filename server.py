from flask import Flask, render_template, request, redirect
import make_sentence, os, twitter
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html', sentence=make_sentence.run())

@app.route('/tweet', methods=['POST'])
def tweet():
    status = request.form['sentence']
    twitter.tweet(status)
    # Returns 400 Bad Request if tweet is longer than 140 characters
    return redirect('/')

if __name__ == '__main__':
    # Required for Heroku's port attachment during deployment
    # Resolved this Error: http://bit.ly/2yRFCqG
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
