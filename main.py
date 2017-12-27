#!C:\Python27\python.exe
# -*- coding: utf-8 -*-

from SocialMediaFactory import SocialMediaFactory
from SocialMedia import SocialMedia
import json
import time


CRYPTONOTE_CURRENCIES = ['bytecoin-bcn', 'boolberry', 'dashcoin', 'digitalnote',
                         'fantomcoin', 'monero', 'quazarcoin', 'aeon']


def save_file(data):
    f = open('data.json', 'w+')
    f.write(json.dumps(data, sort_keys=True, indent=4, separators=(',', ': ')))
    f.close()


def main():
    while True:
        if '00:00' == str(time.strftime("%H:%M")):
            f = open('data.json', 'r')
            senero = json.loads(f.read())
            f.close()

            twitter = SocialMediaFactory.create(SocialMediaFactory.TWITTER, senero)
            instagram = SocialMediaFactory.create(SocialMediaFactory.INSTAGRAM, senero)
            facebook = SocialMediaFactory.create(SocialMediaFactory.FACEBOOK, senero)

            tweets = twitter.get_relevant()
            max_tweets = 50
            counter = 0
            for tweet in tweets:
                senero['twitter']['last_tweet'] = tweet.created_at.strftime("%Y-%m-%d")
                if 'CoinSenero' != tweet.author.screen_name:
                    if counter >= max_tweets:
                        break
                    twitter.update_status(SocialMedia.random_response('@' + str(tweet.author.screen_name)), tweet)
                    print 'Replying to tweet: ' + str(tweet.id)

                    counter += 1
                else:
                    facebook.update_status(tweet.text)
            save_file(senero)

            posts = instagram.get_relevant()
            max_posts = 50
            counter = 0
            for post in posts:
                if counter >= max_posts:
                    break
                instagram.update_status(SocialMedia.random_response(), post)
                print 'Replying to post: ' + str(post['code'])
                counter += 1
            instagram.logout()

            post_txt = SocialMedia.random_post_text()

            print 'New post on Twitter'
            twitter.update_status(post_txt)

            # print 'New post on Instagram'
            # instagram.update_status(post_txt)

            print 'New post on Facebook'
            facebook.update_status(post_txt)


if '__main__' == __name__:
    main()
