from src import clean
import pandas as pd

def test_Clean_text():
    text_df=pd.read_csv("Tweets.csv")
    tweet_clean=clean.TweetClean()
    text_df['text']=text_df['text'].apply(tweet_clean.Clean_text)
    text_df['text'] = text_df['text'].apply(tweet_clean.Standardize_text)
    return text_df['text']
print(test_Clean_text())
