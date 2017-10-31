import make_sentence, twitter, datetime

if __name__ == '__main__':
    today = datetime.date.today()
    print(today)
    # TODO: Implement exponential randomness, make more days preferable than others
    twitter.tweet(make_sentence.run())
    print("Completed Successfully")
