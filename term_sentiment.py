import json
import os
from collections import defaultdict

# ✅ Define file paths directly (modify if needed)
AFINN_FILE = r"C:\Users\jacel\Desktop\Data Science\LAB 2\AFINN-111.txt"
DATA_FILE = r"C:\Users\jacel\Desktop\Data Science\LAB 2\data.json"


def load_afinn(file_path):

    afinn = {}
    if not os.path.exists(file_path):
        print(f"Error: AFINN file not found at {file_path}")
        return afinn  # Return empty dictionary

    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            term, score = line.strip().split("\t")
            afinn[term] = int(score)
    return afinn


def compute_sentiment(afinn, text):

    words = text.lower().split()
    sentiment = sum(afinn.get(word, 0) for word in words)
    return sentiment


def derive_new_terms():

    if not os.path.exists(DATA_FILE):
        print(f"Error: Data file not found at {DATA_FILE}")
        return

    afinn = load_afinn(AFINN_FILE)
    if not afinn:
        print("No sentiment dictionary loaded. Exiting.")
        return

    new_terms = defaultdict(list)

    with open(DATA_FILE, "r", encoding="utf-8") as file:
        tweets = json.load(file)

    for tweet in tweets:
        text = tweet.get("text", "")
        words = text.lower().split()
        sentiment_score = compute_sentiment(afinn, text)

        for word in words:
            if word not in afinn:
                new_terms[word].append(sentiment_score)

    print("\n New term sentiments:\n")
    for term, scores in new_terms.items():
        avg_sentiment = sum(scores) / len(scores)
        print(f"{term} {avg_sentiment:.4f}")


if __name__ == "__main__":
    print("\n Running Sentiment Analysis for New Terms...\n")
    derive_new_terms()
    print("\n✅ Done!")
