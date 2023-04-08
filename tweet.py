import os
import requests
import shutil
import tweepy

# Set Auth + Tweepy
auth = tweepy.OAuthHandler(
    os.environ.get('CONSUMER_KEY'),
    os.environ.get('CONSUMER_SECRET')
)

auth.set_access_token(
    os.environ.get('ACCESS_TOKEN'),
    os.environ.get('ACCESS_SECRET')
)

api = tweepy.API(auth)


# Define tweet_apod
def tweet_apod():
    req = requests.get('https://api.nasa.gov/planetary/apod?api_key=' + os.environ.get('NASA_API_KEY'))
    if req.status_code == 200:
        if req.json()['media_type'] == 'video':
            img_url = (req.json()['thumbnail_url'])
        else:
            img_url = (req.json()['url'])

        title = req.json()['title']
        date = req.json()['date']
        filename = '/tmp/APOD_image.jpg'

        try:
            img_copyright = (req.json()['copyright'])
        except KeyError:
            img_copyright = None

        with open(filename, 'wb') as f:
            shutil.copyfileobj(requests.get(img_url, stream=True).raw, f)

        media = api.media_upload(filename)
        tweet = "Astronomy Picture of the Day\n\nTitle: \"" + title + "\"\nDate: " + date
        if img_copyright is not None:
            tweet += "\nCopyright: " + img_copyright
        api.update_status(status=tweet, media_ids=[media.media_id])
        return 200
    return 500

