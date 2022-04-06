import tweepy
import os

DATABASE_URL = os.environ.get('DATABASE_URL')

auth = tweepy.OAuthHandler(
    os.environ.get('CONSUMER_KEY'),
    os.environ.get('CONSUMER_SECRET')
)

auth.set_access_token(
    os.environ.get('ACCESS_TOKEN'),
    os.environ.get('ACCESS_SECRET')
)

api = tweepy.API(auth)


def tweet_apod(title, date, img, img_copyright):
    media = api.media_upload(img)
    tweet = "Astronomy Picture of the Day\n\nTitle: \"" + title + "\"\nDate: " + date
    if img_copyright is not None:
        tweet += "\nCopyright: " + img_copyright
    api.update_status(status=tweet, media_ids=[media.media_id])
