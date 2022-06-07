import tweepy
import pandas as pd


class CandidateSearch:
    def __init__(self) -> None:
        self.client = tweepy.Client(bearer_token= 'AAAAAAAAAAAAAAAAAAAAAP%2BhdAEAAAAAmQQeypzMWmPjSrNx0U%2Bv0NQHh%2Fc%3DfsPqIoje91MPrmL2yQftjsjeqyXRa3G2uTzJyKRKbOC4OmKGaQ')

    def humber_river(self):
        self.hrbc_riding = {'ONDP':'RakocevicT','OLP':'idalipreti','PCPO':'directorpaul'}
        return self.hrbc_riding
    def hr_id(self):
        self.riding = {'ONDP':'2311077698','OLP':'28800501', 'PCPO':'21759425'}
        return self.riding
    
    def london_north(self):   
        self.lnc_riding = {'ONDP':'kernaghant','OLP':'KateMarieGraham','PCPO':'jerrypribilpc'}
        return self.lnc_riding
    def lnc_id(self):
        self.riding = {'ONDP':'494592983','OLP':'27767093', 'PCPO':'1399126050345476099'}
        return self.riding
        
    def burlington(self):
        self.b_riding = {'OLP':'MariamManaaLib','ONDP':'AD4Burlington', 'GPO':'kylejhutton'}
        return self.b_riding
    def b_id(self):
        self.riding = {'OLP':'2477355842', 'ONDP':'992047554312404992', 'GPO':'155631208'}
        return self.riding
    
    def ajax(self):
        self.a_riding = {'OLP':'AmberBowenforEd','PCPO':'patrice4ajax22','ONDP':'santosforajax'}
        return self.a_riding
    def a_id(self):
        self.riding = {'OLP':'1110193484332437505', 'PCPO':'1494519576956129300', 'ONDP':'1512264594210836514'}
        return self.riding

    def brampton_centre(self):
        self.bc_riding = {'ONDP':'SaraSinghPhD', 'OLP':'VoteSafdarOLP','PCPO':'Charmomof5'}
        return self.bc_riding
    def bc_id(self):
        self.riding = {'ONDP':'468834014','OLP':'960587365826707456', 'PCPO':'702930090'}
        return self.riding  

    def brampton_west(self):
        self.bw_riding = {'PCPO':'sandhuamarjot1','OLP':'RimmyJhajj','ONDP':'Navjitkaurbrar'}
        return self.bw_riding
    def bw_id(self):
        self.riding = {'PCPO':'2870931801', 'OLP':'1360944336368713729', 'ONDP':'1148700903089811461'}
        return self.riding
        
    def vaughn_woodbridge(self):
        self.vw_riding = {'PCPO':'MichaelTibollo','OLP':'StevenDelDuca'}
        return self.vw_riding
    def vw_id(self):
        self.riding = {'PCPO':'1731904891','OLP':'92759522'}
        return self.riding

    def eglinton_lawrence(self):
        self.el_riding = {'PCPO':'RobinMartinPC','OLP':'hebert_arlena', 'ONDP':'DoyleMerrick'}
        return self.el_riding
    def el_id(self):
        self.riding = {'PCPO':'1187004211','OLP':'1027508834493841409', 'ONDP':'1524943425811922957'}
        return self.riding

    def hamilton_east(self):
        '''
        Note: this the incumbent of the Hamilton East riding was removed from NDP cacus and replaced.
        The incumbent, Paul Miller, is now running as an independent.
        '''
        self.he_riding = {'PCPO':'Race_Dad','OLP':'votejasonfarr','ONDP':'ZaighamButtNDP'}
        return self.he_riding
    def he_id(self):
        self.riding = {'PCPO':'3313517385','OLP':'302207954','ONDP':'1516962013649510401'}
        return self.riding

    def parry_sound(self):
        '''
        Note: the NDP candidate for this riding has no social media account and is 
        proxied by the local party account.
        '''
        self.ps_riding = {'ONDP':'PSM_NDP','GPO':'MattRichterGPO','PCPO':'GraydonForMPP'}
        return self.ps_riding
    def ps_id(self):
        self.riding = {'ONDP':'2576801654','GPO':'64602763','PCPO':'172542902'}
        return self.riding

    def get_candidates(self, riding:dict):
        self.candidates_lst = [i for i in riding.values()]
        self.lst = []
        for i in range(len(self.candidates_lst)):
            self.lst.append(self.client.get_user(username = self.candidates_lst[i]))
        return self.lst

    def get_candidates_by_id(self, riding:dict):
        self.candidates_lst = [i for i in riding.values()]
        self.lst = []
        for i in range(len(self.candidates_lst)):
            self.lst.append(self.client.get_user(id = self.candidates_lst[i]))
        return self.lst
        
    def get_tweets(self, id):
        self.lst=[]
        self.tweets = self.lst.append(self.client.get_users_tweets(id, start_time = '2022-05-01T00:00:00Z', max_results = 10))
        return self.lst

    def get_metadata(self, id):
        self.tweets = self.client.get_users_tweets(id, start_time = '2022-05-01T00:00:00Z', max_results = 100)
        return self.tweets[len(self.tweets)-1]
    
    def get_all_tweets(self, id):
        self.lst = []
        self.tweets = self.lst.append(self.client.get_users_tweets(id, start_time = '2022-05-01T00:00:00Z', max_results = 100))
        self.meta = self.get_metadata(id)
        for i in range(10):
            if self.meta['next_token'] == None:
                break
            else:
                self.lst.append(self.client.get_users_tweets(id, pagination_token = self.meta['next_token'], max_results = 100))
                self.meta = self.get_metadata(id)
                i += 1
        return self.lst

    def token_tweet(self, id, token):
        self.token = token
        self.tweets = self.client.get_users_tweets(id, pagination_token = self.token, max_results = 5)
        self.metadata = self.tweets[len(self.tweets)-1]
        self.tweet_token = self.metadata['next_token']
    
    def get_token_from_tweet(self, tweet):
        self.tweet = tweet
        self.metadata = self.tweet[len(self.tweet)-1]
        self.tweet_token = self.metadata['next_token']
        return self.tweet_token
    
    def get_tweet_v2(self, id):
        self.tweet = self.client.get_users_tweets(id, start_time = '2022-05-01T00:00:00Z', max_results = 10)
        self.token = self.get_token_from_tweet(self.tweet)
        return self.tweet, self.token
    
    def get_all_tweets_v2(self, id):
        self.twt_lst = []
        self.first_query = self.client.get_users_tweets(id, start_time = '2022-05-01T00:00:00Z', max_results = 100)
        self.twt_lst.append(self.first_query)
        i = 0
        while i < 4:
            try:
                self.token = self.get_token_from_tweet(self.first_query)
                print(f"Downloading Page {i+1}")
                self.tweet = self.client.get_users_tweets(id, pagination_token= self.token, max_results = 100)
                i+=1
                self.twt_lst.append(self.tweet)
                self.token = self.get_token_from_tweet(self.tweet)
            except KeyError:
                print("no more tokens")
                i = 5
        return self.twt_lst
    
    def get_original_tweets(self,id=str):
        '''
        Gets 500 og tweets (no retweets) from the candidate, starting on 
        May 1st, 2022.
        '''
        self.twt_lst = []
        i = 0
        while i < 20:
            try:
                if i == 0:
                    print(f"Downloading page {i+1}")
                    self.query = self.client.get_users_tweets(id, start_time = '2022-05-02T00:00:00Z', max_results = 100, exclude = "retweets")
                    self.twt_lst.append(self.query)
                    self.token = self.get_token_from_tweet(self.query)
                    i+=1
                else:
                    print(f"Downloading page {i+1}")
                    self.tweet = self.client.get_users_tweets(id, pagination_token= self.token, max_results = 100, exclude = "retweets")
                    self.twt_lst.append(self.tweet)
                    i += 1
                    self.token = self.get_token_from_tweet(self.query)
            except KeyError:
                print("No more Tokens")
                i=21
        return self.twt_lst

    def get_original_tweets_v2(self,id=str): # Come back and fix this.
        '''
        Gets all og tweets (no retweets) from the candidate, starting on 
        May 1st, 2022.
        '''
        self.twt_lst = []
        i = 0
        while i < 100:
            try:
                if i == 0:
                    print(f"Downloading page {i+1}")
                    self.query = self.client.get_users_tweets(id, start_time = '2022-05-02T00:00:00Z', max_results = 100, exclude = "retweets")
                    self.twt_lst.append(self.query)
                    self.token = self.get_token_from_tweet(self.query)
                    i+=1
                else:
                    print(f"Downloading page {i+1}")
                    self.tweet = self.client.get_users_tweets(id, pagination_token= self.token, max_results = 100, exclude = "retweets")
                    self.twt_lst.append(self.tweet)
                    i += 1
                    self.token = self.get_token_from_tweet(self.query)          
            except KeyError:
                print("No more Tokens")
                i = 101
        return self.twt_lst
    
    def get_original_tweets_v3(self,id=str):
        self.twt_lst = []
        self.date_lst = ['2022-05-01T00:00:00Z','2022-05-02T00:00:00Z','2022-05-03T00:00:00Z','2022-05-04T00:00:00Z','2022-05-05T00:00:00Z','2022-05-06T00:00:00Z','2022-05-07T00:00:00Z','2022-05-08T00:00:00Z']
        k = 0
        for i in self.date_lst:
            self.query = self.client.get_users_tweets(id, start_time = i, end_time = self.date_lst[k+1], max_results = 100, exclude = "retweets")
            self.twt_lst.append(self.query)
            k += 1

    def date_constructor_v2(self, date):
        self.full_date = date
        self.date = self.full_date[:10]
        self.time = self.full_date[10:]
        self.end_time = self.date + 'T23:59:59Z'
        print(f"Start date: {self.full_date}\nEnd date: {self.end_time}")
    
    def get_tweets_from_date(self,id,date):
        '''(str, str)->lst
        Date format = '2022-05-01T00:00:00Z'
        '''
        self.twt_lst = []
        self.meta_lst = []
        self.end_date = date[:10] + 'T23:59:59Z'
        self.query = self.client.get_users_tweets(id, start_time = date, end_time = self.end_date, max_results = 100, exclude = "retweets")
        self.metadata = int(self.query[len(self.query)-1]['result_count'])
        self.twt_lst.append(self.query)
        self.meta_lst.append(self.metadata)
        return self.meta_lst
        #return self.twt_lst
    
    def get_campaign_tweet_sum(self, id):
        self.week1 =['2022-05-01T00:00:00Z','2022-05-02T00:00:00Z','2022-05-03T00:00:00Z','2022-05-04T00:00:00Z','2022-05-05T00:00:00Z','2022-05-06T00:00:00Z','2022-05-07T00:00:00Z']
        self.week2 =['2022-05-08T00:00:00Z','2022-05-09T00:00:00Z','2022-05-10T00:00:00Z','2022-05-11T00:00:00Z','2022-05-12T00:00:00Z','2022-05-13T00:00:00Z','2022-05-14T00:00:00Z']
        self.week3 =['2022-05-15T00:00:00Z','2022-05-16T00:00:00Z','2022-05-17T00:00:00Z','2022-05-18T00:00:00Z','2022-05-19T00:00:00Z','2022-05-20T00:00:00Z','2022-05-21T00:00:00Z']
        self.week4 =['2022-05-22T00:00:00Z','2022-05-23T00:00:00Z','2022-05-24T00:00:00Z','2022-05-25T00:00:00Z','2022-05-26T00:00:00Z','2022-05-27T00:00:00Z','2022-05-28T00:00:00Z']
        self.week5 =['2022-05-29T00:00:00Z','2022-05-30T00:00:00Z','2022-05-31T00:00:00Z','2022-06-01T00:00:00Z']
        self.campaign = [self.week1, self.week2, self.week3, self.week4, self.week5]
        self.accum = 0
        self.twt_lst = [self.get_tweets_from_date(id, date) for date in self.week1]+[self.get_tweets_from_date(id, date) for date in self.week2]+[self.get_tweets_from_date(id, date) for date in self.week3]+[self.get_tweets_from_date(id, date) for date in self.week4]+[self.get_tweets_from_date(id, date) for date in self.week5]
        for i in range(len(self.twt_lst)-1):
            self.accum += self.twt_lst[i][0]
        return self.accum
    
    def get_retweets_from_date(self,id,date):
        '''(str, str)->lst
        Date format = '2022-05-01T00:00:00Z'
        '''
        self.twt_lst = []
        self.meta_lst = []
        self.end_date = date[:10] + 'T23:59:59Z'
        self.query = self.client.get_users_tweets(id, start_time = date, end_time = self.end_date, max_results = 100)
        self.metadata = int(self.query[len(self.query)-1]['result_count'])
        self.twt_lst.append(self.query)
        self.meta_lst.append(self.metadata)
        return self.meta_lst

    def get_campaign_retweet_sum(self, id):
        self.week1 =['2022-05-01T00:00:00Z','2022-05-02T00:00:00Z','2022-05-03T00:00:00Z','2022-05-04T00:00:00Z','2022-05-05T00:00:00Z','2022-05-06T00:00:00Z','2022-05-07T00:00:00Z']
        self.week2 =['2022-05-08T00:00:00Z','2022-05-09T00:00:00Z','2022-05-10T00:00:00Z','2022-05-11T00:00:00Z','2022-05-12T00:00:00Z','2022-05-13T00:00:00Z','2022-05-14T00:00:00Z']
        self.week3 =['2022-05-15T00:00:00Z','2022-05-16T00:00:00Z','2022-05-17T00:00:00Z','2022-05-18T00:00:00Z','2022-05-19T00:00:00Z','2022-05-20T00:00:00Z','2022-05-21T00:00:00Z']
        self.week4 =['2022-05-22T00:00:00Z','2022-05-23T00:00:00Z','2022-05-24T00:00:00Z','2022-05-25T00:00:00Z','2022-05-26T00:00:00Z','2022-05-27T00:00:00Z','2022-05-28T00:00:00Z']
        self.week5 =['2022-05-29T00:00:00Z','2022-05-30T00:00:00Z','2022-05-31T00:00:00Z','2022-06-01T00:00:00Z']
        self.campaign = [self.week1, self.week2, self.week3, self.week4, self.week5]
        self.accum = 0
        self.twt_lst = [self.get_retweets_from_date(id, date) for date in self.week1]+[self.get_retweets_from_date(id, date) for date in self.week2]+[self.get_retweets_from_date(id, date) for date in self.week3]+[self.get_retweets_from_date(id, date) for date in self.week4]+[self.get_retweets_from_date(id, date) for date in self.week5]
        for i in range(len(self.twt_lst)-1):
            self.accum += self.twt_lst[i][0]
        return self.accum


