'''
Responsible to upload a image file to twitter
'''

from TwitterAPI import TwitterAPI

def uploadToTwitter(imagePath, profile):

	TWEET_TEXT = 'This is test image upload from Raspberry pi Wheezy - piHome automation - IoT team'
	IMAGE_PATH = imagePath 

	CONSUMER_KEY = profile['twitter_access']['CONSUMER_KEY'] 
	CONSUMER_SECRET = profile['twitter_access']['CONSUMER_SECRET'] 
	ACCESS_TOKEN_KEY = profile['twitter_access']['ACCESS_TOKEN_KEY'] 
	ACCESS_TOKEN_SECRET = profile['twitter_access']['ACCESS_TOKEN_SECRET'] 

	api = TwitterAPI(CONSUMER_KEY,
                 CONSUMER_SECRET,
                 ACCESS_TOKEN_KEY,
                 ACCESS_TOKEN_SECRET)

	file = open(IMAGE_PATH, 'rb')
	data = file.read()
	r = api.request('statuses/update_with_media',
                {'status': TWEET_TEXT},
                {'media[]': data})

	return 'Successfully posted image in Twitter.' if r.status_code == 200 else 'Something went wrong, please try again'

