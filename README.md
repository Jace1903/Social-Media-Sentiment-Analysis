Social Media Sentiment Analysis  
========================================

Author: Jace Lopes  
Date: 02/24/2025

----------------------------------------
OVERVIEW
----------------------------------------
This project explores sentiment analysis and data processing for a collection of tweets. It demonstrates the use of basic natural language processing techniques, including sentiment scoring, term frequency analysis, new term sentiment derivation, and hashtag extraction.

----------------------------------------
PROJECT FILES
----------------------------------------

- data.json  
  Main tweet dataset. Contains tweets in JSON array format.

- AFINN-111.txt  
  Sentiment lexicon: wordscore.

- scraper.py  
  Script to scrape up to 100 recent tweets with selected sentiment keywords from Twitter API v2 (Tweepy).

- tweet_sentiment.py  
  Script to compute and print sentiment scores for each tweet using AFINN-111.txt.

- term_sentiment.py  
  Assigns and prints sentiment scores to words not found in AFINN, based on their context in tweets.

- Frequency.py  
  Calculates and prints the relative frequency of each word in the tweet dataset.

- happiest_state.py  
  Attempts to identify the happiest US state by average sentiment (requires tweets with valid location or place metadata).

- top_ten.py  
  Extracts and prints the top 10 most used hashtags (requires hashtag metadata).

- Lab-02-Report.pdf  
  Overview and result documentation for all tasks.


----------------------------------------
DEPENDENCIES & REQUIREMENTS
----------------------------------------
- Python 3.12 or later
- Libraries: tweepy, json, os, re, collections
- Twitter API credentials (required for scraping new data)

----------------------------------------
HOW TO RUN
----------------------------------------

1. (Optional) Collect new tweets:
   - Update Twitter API credentials in scraper.py.
   - Run scraper.py to save tweets as data.json.

2. Sentiment analysis for tweets:
   - Run tweet_sentiment.py (prints one sentiment score per tweet).

3. New term sentiment assignment:
   - Run term_sentiment.py (displays sentiment estimates for previously unseen words).

4. Term frequency calculation:
   - Run Frequency.py (prints each word's relative frequency in data.json).

5. Happiest state analysis:
   - Run happiest_state.py (prints the state with the highest average sentiment, if any valid state metadata present).

6. Top 10 hashtags:
   - Run top_ten.py (prints the most frequent hashtags from tweets, if hashtag metadata present).

----------------------------------------
NOTES
----------------------------------------
- All scripts rely on disk file paths – modify as appropriate for your directory structure.
- Sentiment scoring relies on the AFINN-111 lexicon.
- Only English-language tweets are scraped.
- Hashtag and state analysis rely on respective fields existing in tweet data (geo/entities metadata required for full output).
- See Lab-02-Report.pdf for workflow explanations and sample script outputs.

----------------------------------------
CONTACT
----------------------------------------
Questions or suggestions?  
Contact: Jace Lopes

----------------------------------------
END OF README
----------------------------------------

[1] https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/10126181/7f75128b-398d-4a34-872b-42e52f1714c4/data.json
[2] https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/10126181/1dae58b2-7c78-46d8-9a15-f69f04c95914/Frequency.py
[3] https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/10126181/b0671ad0-2f6f-4b92-8516-74f916fc1327/happiest_state.py
[4] https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/10126181/4abbc49d-38cb-4568-9a08-28555e4bb9d8/Lab-02-Report.pdf
[5] https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/10126181/6176b007-21c6-49b3-9975-e9302b29bcea/scraper.py
[6] https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/10126181/d68297d6-c84c-4082-857b-4163944db6c8/term_sentiment.py
[7] https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/10126181/9b2311b7-5c07-4017-95eb-0a50efd262e0/top_ten.py
[8] https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/10126181/941f7465-62f4-4e89-bf7e-c38f367379a4/tweet_sentiment.py
