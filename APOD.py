import requests
import shutil
import db_controller
import tweet
import os

req = requests.get('https://api.nasa.gov/planetary/apod?api_key=' + os.environ.get('NASA_API_KEY'))
if req.status_code == 200:
    if req.json()['media_type'] == 'video':
        img_url = (req.json()['thumbnail_url'])
    else:
        img_url = (req.json()['url'])

    title = req.json()['title']
    date = req.json()['date']
    filename = 'APOD_image.jpg'

    try:
        img_copyright = (req.json()['copyright'])
    except KeyError:
        img_copyright = None

    with open(filename, 'wb') as f:
        shutil.copyfileobj(requests.get(img_url, stream=True).raw, f)

    tweet.tweet_apod(title, date, filename, img_copyright)
    db_controller.insert_into_db('apod', title, date, img_url, img_copyright)
