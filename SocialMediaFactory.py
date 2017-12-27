#!C:\Python27\python.exe
# -*- coding: utf-8 -*-

from SocialMedias.Twitter import Twitter
from SocialMedias.Instagram import Instagram
from SocialMedias.Facebook import Facebook


class SocialMediaFactory(object):
    TWITTER = 'twitter'
    INSTAGRAM = 'instagram'
    FACEBOOK = 'facebook'

    @staticmethod
    def create(name, senero):
        if SocialMediaFactory.TWITTER == name:
            return Twitter(senero)
        elif SocialMediaFactory.INSTAGRAM == name:
            return Instagram(senero)
        elif SocialMediaFactory.FACEBOOK == name:
            return Facebook(senero)
