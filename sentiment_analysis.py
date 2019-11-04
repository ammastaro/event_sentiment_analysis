import pandas as pd
import numpy as np
from textblob import TextBlob
import math
import json


df = pd.read_csv("Reddit_Sandy.csv")

reddit_sandy_sentiments = []

for i in range (0,df.shape[0]):
    print("{0} / {1}".format(i, df.shape[0]))
    if type(df.iloc[i][1]) is str:
        blob = TextBlob(df.iloc[i][1])
        for sentence in blob.sentences:
            reddit_sandy_sentiments.append(sentence.sentiment.subjectivity)

rss_df = pd.DataFrame(reddit_sandy_sentiments)

rss_df.to_csv("reddit_sandy_subject.csv")


df2 = pd.read_excel("Twitter_Sandy.xls")

arr = list(df2.columns)
arr[0] = "tweet"
df2.columns = arr
df2 = df2[["tweet"]]
twitter_sandy_sentiments = []

for i in range (0,df2.shape[0]):
    print("{0} / {1}".format(i, df2.shape[0]))
    tweet = df2.iloc[i][0]
    tweet = tweet[9:] #this cuts u'{text.. prefix
    if u'#' in tweet:
        tweet.join(filter(lambda x:x[0]!='#', tweet.split()))
    if u'@' in tweet:
        tweet.join(filter(lambda x:x[0]!='@', tweet.split()))
    if u'http' in tweet:
        tweet.join(filter(lambda x:x[0]!='http', tweet.split()))
    blob = TextBlob(tweet)
    for sentence in blob.sentences:
        twitter_sandy_sentiments.append(sentence.sentiment.subjectivity)

tss_df = pd.DataFrame(twitter_sandy_sentiments)

tss_df.to_csv("twitter_sandy_subject.csv")

df3 = pd.read_excel("Twitter_Elections.xls")

arr = list(df3.columns)
arr[0] = "tweet"
df3.columns = arr
df3 = df3[["tweet"]]
twitter_obama_sentiments = []

for i in range (0,df3.shape[0]):
    print("{0} / {1}".format(i, df3.shape[0]))
    tweet = df3.iloc[i][0]
    if type(tweet) != float:
        if u'#' in tweet:
            tweet.join(filter(lambda x:x[0]!='#', tweet.split()))
        if u'@' in tweet:
            tweet.join(filter(lambda x:x[0]!='@', tweet.split()))
        if u'http' in tweet:
            tweet.join(filter(lambda x:x[0]!='http', tweet.split()))
        blob = TextBlob(tweet)
        for sentence in blob.sentences:
            twitter_obama_sentiments.append(sentence.sentiment.subjectivity)

tos_df = pd.DataFrame(twitter_obama_sentiments)

tos_df.to_csv("twitter_obama_subject.csv")

#RC_2012-08
subs = pd.read_csv("PoliticalSubreddits.csv")
subreddits = list(subs.columns)

comments = []
count = 0
with open("RC_2012-08", "rb") as f:
    for line in f:
        print("{0} / {1}".format(len(comments), count))
        obj = json.loads(line)
        if obj["subreddit"] in subreddits:
            comments.append(obj["body"])
        if len(comments) >= 5000:
            break
        count = count + 1

reddit_obama_sentiments = []

for i in range (0, len(comments)):
    print("{0} / {1}".format(i, len(comments)))
    blob = TextBlob(comments[i])
    for sentence in blob.sentences:
        reddit_obama_sentiments.append(sentence.sentiment.subjectivity)

ros_df = pd.DataFrame(reddit_obama_sentiments)

ros_df.to_csv("reddit_obama_subject.csv")
