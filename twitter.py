import os, sys, dotenv
dotenv.load_dotenv('.env')

consumer_key = os.environ.get('TWITTER_CONSUMER_KEY')
consumer_secret = os.environ.get('TWITTER_CONSUMER_SECRET')
access_token = os.environ.get('TWITTER_ACCESS_TOKEN')
access_token_secret = os.environ.get('TWITTER_ACCESS_TOKEN_SECRET')

from requests_oauthlib import OAuth1Session

# Create Authentication Session
session = OAuth1Session(consumer_key, client_secret=consumer_secret,
            resource_owner_key=access_token, resource_owner_secret=access_token_secret)

# Contents of Status (i.e. tweet text)
status = "If you are reading this on Twitter, the API request worked!"

def tweet(status):
    # URL Endpoint to update status
    url = "https://api.twitter.com/1.1/statuses/update.json"
    # POST request to url with 'status' parameter
    resp = session.post(url, {'status': status})
    # Show text from response to POST request
    return resp.text

if __name__ == '__main__':
    status = sys.argv
    status.pop(0)
    print(tweet(" ".join(status)))
