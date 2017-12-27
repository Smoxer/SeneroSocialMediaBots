#!C:\Python27\python.exe
# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod
import urllib2
import json
import random


class SocialMedia(object):
    CRYPTONOTE_CURRENCIES = ['bytecoin-bcn', 'boolberry', 'dashcoin', 'digitalnote',
                             'fantomcoin', 'monero', 'quazarcoin', 'aeon']
    __metaclass__ = ABCMeta

    @abstractmethod
    def __init__(self, senero):
        pass

    @abstractmethod
    def get_relevant(self):
        pass

    @abstractmethod
    def update_status(self, txt, post=None):
        pass

    @staticmethod
    def symbol_to_id(*coin_symbols):
        response = urllib2.urlopen('https://api.coinmarketcap.com/v1/ticker/?convert=EUR&limit=0').read()
        coins = json.loads(response)
        current_coin = {}
        for coin_symbol in coin_symbols:
            for coin in coins:
                if coin_symbol.lower() == coin['symbol'].lower() or coin_symbol.lower() == coin['id']:
                    current_coin[coin_symbol.lower()] = coin
                    break
        return current_coin

    @staticmethod
    def random_response(text_before=''):
        secure_random = random.SystemRandom()
        txt = text_before + '#' + secure_random.choice(['monero', 'xmr']) + \
            ' fees are $' + secure_random.choice(['5', '6', '7', '8']) + ' on average, #senero is the scalable 2 ' \
                                                                         'chain solution ' + secure_random.choice(
            ['http://t.me/senero',
             '@coinsenero',
             'senero.org',
             'senero.org/blog',
             'reddit.com/r/senero']
        ) + ' to help us deliver ' + secure_random.choice(
            ['blind #smartcontracts', 'secure applications #Sapps', '#attentionbidding', '#SICOs']) + \
            '\n\n#Senero looking to #ETC for ICO, #ETH seems to centralized.'
        return txt

    @staticmethod
    def random_post_text():
        coins = SocialMedia.symbol_to_id(*SocialMedia.CRYPTONOTE_CURRENCIES)
        sum_coins = 0
        for coin in coins:
            coin = coins[coin]
            sum_coins += float(coin['market_cap_usd'])
        avg = str(int(sum_coins) / len(SocialMedia.CRYPTONOTE_CURRENCIES))
        sum_coins = str('{:,}'.format(int(sum_coins))) + '$'
        avg = str('{:,}'.format(int(avg))) + '$'
        post_txt = 'Current cryptonote market cap is: ' + sum_coins + \
                   '\nhttps://t.me/senero\n\nAverage cost per cryptonote coin: ' + avg \
                   + '\nhttps://t.me/senero\n#senero #' \
                   + ' #'.join(SocialMedia.CRYPTONOTE_CURRENCIES).replace('-bcn', '')
        return post_txt
