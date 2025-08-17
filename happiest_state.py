import json
import os
from collections import defaultdict

# Define file paths
DATA_FILE = r"C:\Users\jacel\Desktop\Data Science\LAB 2\data1.json"
AFINN_FILE = r"C:\Users\jacel\Desktop\Data Science\LAB 2\AFINN-111.txt"

def load_afinn():

    afinn = {}
    try:
        with open(AFINN_FILE, "r", encoding="utf-8") as file:
            for line in file:
                parts = line.strip().split("\t")
                if len(parts) == 2:
                    word, score = parts
                    afinn[word] = int(score)
        print(f"Loaded {len(afinn)} words from AFINN-111.txt")
    except FileNotFoundError:
        print("Error: AFINN-111.txt file not found.")
    return afinn

def calculate_sentiment(tweet_text, afinn):
    """Calculate sentiment score of a tweet based on AFINN words."""
    words = tweet_text.lower().split()
    return sum(afinn.get(word, 0) for word in words)

def extract_state(tweet):

    if "user" in tweet and "location" in tweet["user"]:
        location = tweet["user"]["location"]
        if location:
            return location[-2:].upper()  # Assumes last 2 characters indicate the state (e.g., "CA", "NY")
    return None

def find_happiest_state():

    if not os.path.exists(DATA_FILE):
        print(f"Error: Data file not found at {DATA_FILE}")
        return

    afinn = load_afinn()
    if not afinn:
        return

    state_sentiments = defaultdict(list)

    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            for line in file:
                try:
                    tweet = json.loads(line.strip())  # Load each JSON object
                    if "text" in tweet:
                        state = extract_state(tweet)
                        if state:
                            sentiment = calculate_sentiment(tweet["text"], afinn)
                            state_sentiments[state].append(sentiment)
                except json.JSONDecodeError as e:
                    print(f"Skipping malformed JSON line: {e}")

    except Exception as e:
        print(f"Error reading file: {e}")
        return

    if not state_sentiments:
        print("No valid states found in dataset.")
        return

    # Compute average sentiment per state
    state_avg_sentiment = {state: sum(scores) / len(scores) for state, scores in state_sentiments.items()}

    # Find the happiest state
    happiest_state = max(state_avg_sentiment, key=state_avg_sentiment.get)
    print(f"\nHappiest State: {happiest_state} with average sentiment score {state_avg_sentiment[happiest_state]:.2f}")

if __name__ == "__main__":
    print("\nRunning Happiest State Analysis...\n")
    find_happiest_state()
    print("\nDone!")
