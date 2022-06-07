import tweepy

client = tweepy.Client(bearer_token= 'AAAAAAAAAAAAAAAAAAAAAM7qcQEAAAAAWJIwAdbviPjZfOdWmBIWzR0iK%2Bw%3D7VaqEuVUMKg7KXK65A8Hu3JUfWwXKce4ifxImzYfUiVIdX2miq')

on_poli_query = "#onpoli -is:retweet lang:en"

tweets = client.search_recent_tweets(query = on_poli_query, tweet_fields=['context_annotations', 'created_at'], max_results=25)

for tweet in tweets.data:
    print(tweet.text)
    if len(tweet.context_annotations) > 0:
        print(tweet.context_annotations)

