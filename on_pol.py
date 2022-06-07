import tweepy

client = tweepy.Client(bearer_token= 'AAAAAAAAAAAAAAAAAAAAAM7qcQEAAAAAWJIwAdbviPjZfOdWmBIWzR0iK%2Bw%3D7VaqEuVUMKg7KXK65A8Hu3JUfWwXKce4ifxImzYfUiVIdX2miq')
humber_river = ['idalipreti','directorpaul','RakocevicT']

def get_candidates(riding:list):
    for i in riding:
        c = client.get_user(username = i)
        print(c)

client.search_all_tweets()