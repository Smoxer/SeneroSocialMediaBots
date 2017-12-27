#!C:\Python27\python.exe
# -*- coding: utf-8 -*-

from SocialMedia import SocialMedia
import facebook


class Facebook(SocialMedia):
    def __init__(self, senero):
        self.senero = senero
        self.graph = facebook.GraphAPI(senero['facebook']['access_token'])

        super(Facebook, self).__init__(senero)

    def get_relevant(self):
        return None

    def update_status(self, txt, post=None):
        self.graph.put_wall_post(txt)
