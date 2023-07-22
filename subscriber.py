from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from oauth2client.tools import argparser

def get_subscribed_channels(api_key):
    youtube = build('youtube', 'v3', developerKey=api_key)

    try:
        channels = []
        next_page_token = None

        while True:
            response = youtube.subscriptions().list(
                part='snippet',
                channelId='aikanshpriyam3977',
                maxResults=50,
                pageToken=next_page_token
            ).execute()

            channels.extend(response['items'])

            next_page_token = response.get('nextPageToken')

            if not next_page_token:
                break

        return channels

    except HttpError as e:
        print('An error occurred:', e)

# Set your API key
API_KEY = 'AIzaSyClqemp2grayXy0jxzZjU2x4ooBT4fq0zs'

# Call the function to get subscribed channels
subscribed_channels = get_subscribed_channels(API_KEY)

# Print the channel titles
for channel in subscribed_channels:
    print(channel['snippet']['title'])
