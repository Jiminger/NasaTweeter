# NasaTweeter

### Description ###
This is an application that retrieves the Astronomy Picture of the Day (APOD) provided by the NASA Open APIs 
and posts it to [Twitter](https://twitter.com/NasaTweeter) using the Tweepy library.  
The code is hosted on AWS Lambda and is triggered by a CloudWatch event every day at 7am EST.

#### Important Files: ####
- **tweet.py**: module that handles the retrieval of APOD and subsequent posting to twitter.
- **lambda_function.py**: module containing the Lambda function handler that processes events.
- **layer/python.zip**: ZIP archive that contains additional dependencies needed for the application. 
