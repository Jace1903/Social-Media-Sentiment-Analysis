import json


def load_afinn(file_path):

    afinn = {}
    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            term, score = line.strip().split("\t")
            afinn[term] = int(score)
    return afinn


def compute_sentiment(afinn, text):

    words = text.lower().split()  # Convert to lowercase and tokenize words
    sentiment = sum(afinn.get(word, 0) for word in words)  # Sum sentiment scores
    return sentiment


def analyze_tweets():

    # Define file paths
    afinn_file = "C:\\Users\\jacel\\Desktop\\Data Science\\LAB 2\\AFINN-111.txt"
    data_file = "C:\\Users\\jacel\\Desktop\\Data Science\\LAB 2\\data.json"

    afinn = load_afinn(afinn_file)  # Load AFINN dictionary

    # Open the scraped tweet data file
    with open(data_file, "r", encoding="utf-8") as file:
        tweets = json.load(file)  # Load tweets from JSON file

    # Process each tweet
    for tweet in tweets:
        text = tweet.get("text", "")  # Extract tweet text
        sentiment_score = compute_sentiment(afinn, text)  # Compute sentiment
        print(sentiment_score)  # Print one sentiment score per tweet


if __name__ == "__main__":
    analyze_tweets()  # Run sentiment analysis
