import json
import os
from collections import Counter

# Define the file path
DATA_FILE = r"C:\Users\jacel\Desktop\Data Science\LAB 2\data1.json"

def extract_hashtags(tweet):

    hashtags = []
    if isinstance(tweet, dict) and "entities" in tweet and "hashtags" in tweet["entities"]:
        hashtags = [tag["text"].lower() for tag in tweet["entities"]["hashtags"]]
    return hashtags

def find_top_hashtags():

    if not os.path.exists(DATA_FILE):
        print(f"Error: Data file not found at {DATA_FILE}")
        return

    hashtag_counts = Counter()

    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            # Read JSON line by line to handle JSONL format
            for line in file:
                try:
                    tweet = json.loads(line.strip())  # Load each JSON object
                    hashtags = extract_hashtags(tweet)
                    hashtag_counts.update(hashtags)
                except json.JSONDecodeError as e:
                    print(f"Skipping malformed JSON line: {e}")

    except Exception as e:
        print(f"Error reading file: {e}")
        return

    if not hashtag_counts:
        print("No hashtags found in dataset.")
        return

    # Get the top 10 most common hashtags
    top_hashtags = hashtag_counts.most_common(10)

    print("\nTop 10 Hashtags:\n")
    for tag, count in top_hashtags:
        print(f"{tag} {count}")

if __name__ == "__main__":
    print("\nRunning Top 10 Hashtags Analysis...\n")
    find_top_hashtags()
    print("\nDone!")
