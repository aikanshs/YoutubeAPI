import googleapiclient.discovery

youtube = googleapiclient.discovery.build(
    "youtube", "v3", developerKey="AIzaSyA-lN3BNkE0hWWiaWIT3jEA4q4XAafg8qY")

def get_subscriptions(channel_id):
  """Gets a list of all the channels the specified user is subscribed to."""

  request = youtube.subscriptions().list(
    part="snippet",
    channelId=channel_id,
    maxResults=500,
  )
  response = request.execute()

  return response["items"]

def main():
  channel_id = "UCnN6MvOGxcFPhjQxriX2ISQ"
  subscriptions = get_subscriptions(channel_id)
  print("Num of Subscribers:", len(subscriptions))
  for subscription in subscriptions:
    print(subscription)

if __name__ == "__main__":
  main()
