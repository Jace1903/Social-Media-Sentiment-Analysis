import tweepy
import json

# Twitter API credentials (Replace with your own)
BEARER_TOKEN = "AAAAAAAAAAAAAAAAAAAAAHQnzgEAAAAACzSirwX4xygt5iuBWuPvWzfSPSI%3DLCe0R4gW4fJ2YLO1t8MUSRYJYhgXQ1r5q7rLE8MLEXalk1o0Ic"

# Authenticate with Twitter API v2
client = tweepy.Client(bearer_token=BEARER_TOKEN)

# Define search query (only English tweets, no retweets)
query = "happy OR sad OR excited OR angry -is:retweet lang:en"

# Fetch recent tweets (max 100)
tweets = client.search_recent_tweets(query=query, max_results=100, tweet_fields=["created_at", "geo"])

# Save tweets to a JSON file
output_file = "data.json"
tweet_data = []

for tweet in tweets.data:
    tweet_info = {
        "id": tweet.id,
        "text": tweet.text,
        "created_at": tweet.created_at.isoformat(),
        "geo": tweet.geo  # Location information
    }
    tweet_data.append(tweet_info)

# Write to JSON file
with open(output_file, "w", encoding="utf-8") as file:
    json.dump(tweet_data, file, indent=4)

print("Data collection complete! Tweets saved to", output_file)
