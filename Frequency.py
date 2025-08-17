import json
import os
import re
from collections import Counter

# ✅ Define the file path directly (modify if needed)
DATA_FILE = r"C:\Users\jacel\Desktop\Data Science\LAB 2\data.json"


def clean_text(text):

    text = text.lower()  # Convert to lowercase
    text = re.sub(r"http\S+", "", text)  # Remove URLs
    text = re.sub(r"[^\w\s]", "", text)  # Remove punctuation
    words = text.split()  # Tokenize text into words
    return words


def compute_term_frequency():

    if not os.path.exists(DATA_FILE):
        print(f"Error: Data file not found at {DATA_FILE}")
        return

    term_counts = Counter()
    total_terms = 0

    # Load tweets from JSON file
    with open(DATA_FILE, "r", encoding="utf-8") as file:
        tweets = json.load(file)

    # Process each tweet
    for tweet in tweets:
        words = clean_text(tweet.get("text", ""))
        term_counts.update(words)
        total_terms += len(words)

    if total_terms == 0:
        print(" No words found in tweets.")
        return

    print("\n Term Frequencies:\n")
    for term, count in term_counts.items():
        frequency = count / total_terms
        print(f"{term} {frequency:.6f}")  # Print term and its frequency


if __name__ == "__main__":
    print("\n Running Term Frequency Analysis...\n")
    compute_term_frequency()
    print("\n Done!")
