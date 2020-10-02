#!/usr/bin/env python
# coding: utf-8

# In[1]:


#importing needed libraries
import os
import tweepy as tw
import pandas as pd


# In[2]:


#Variables that contains the user credentials to access Twitter API 
consumer_key = os.environ.get('TWITTER_API_KEY')
consumer_secret = os.environ.get('TWITTER_API_SECRET')
access_token = os.environ.get('TWITTER_ACCESS_TOKEN')
access_token_secret = os.environ.get('TWITTER_ACCESS_TOKEN_SECRET')



# In[3]:


#loading our twitter api credentials
auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth, wait_on_rate_limit=True)


# In[4]:


def data_download(keyword_list,date_since):
    """"This function downloads tweets based on keywords and saves then to their own csv files

    Args: Keyword_list - This is a list of keywords
        : date_since - date from which you want to collect the tweets

    """

    for keyword in keyword_list:
        #downloads the given number of tweets
        tweets = tw.Cursor(api.search,q=keyword,since=date_since).items(1000000)
        # Iterate and print tweets
        tweet_data = [[tweet.user.screen_name,tweet.created_at, tweet.user.location,tweet.text] for tweet in tweets]
        tweet_text = pd.DataFrame(data=tweet_data, columns=["user","time", "location","text"])
        # save words to csv file for individual key word
        tweet_text.to_csv('{keyword}.csv'.format(keyword=keyword))


# In[ ]:


#list of keywords to download
keyword_list = ['food_prices','expiry_dates','junk_food','vegetables','diet','food poisoning']
data_download(keyword_list,"2020-04-16")


# In[ ]:




