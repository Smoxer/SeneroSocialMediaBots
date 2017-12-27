#!C:\Python27\python.exe
# -*- coding: utf-8 -*-

from SocialMedia import SocialMedia
import tweepy


class Twitter(SocialMedia):
    def __init__(self, senero):
        self.senero = senero
        auth = tweepy.OAuthHandler(senero['twitter']['consumer_key'], senero['twitter']['consumer_secret'])
        auth.set_access_token(senero['twitter']['access_token'], senero['twitter']['access_token_secret'])
        self.api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

        super(Twitter, self).__init__(senero)

    def get_relevant(self):
        tweets = []
        for tweet in tweepy.Cursor(self.api.search,
                                   q='#senero OR #monero',
                                   since=self.senero['twitter']['last_tweet'],
                                   rpp=50,
                                   include_entities=True).items():
            tweets.append(tweet)
        return tweets[::-1]

    def update_status(self, txt, post=None):
        tweet_id = None
        if post is not None:
            tweet_id = post.id
        self.api.update_status(
            status=txt,
            in_reply_to_status=tweet_id
        )
