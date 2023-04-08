import json
import tweet


def lambda_handler(event, context):

    status = tweet.tweet_apod()
    if status == 200:
        return {
            'statusCode': 200,
            'body': json.dumps('Image posted successfully.')
        }
    else:
        return {
            'statusCode': 500,
            'body': json.dumps('An unknown error occurred.')
        }

