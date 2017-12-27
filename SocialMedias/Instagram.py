#!C:\Python27\python.exe
# -*- coding: utf-8 -*-

from SocialMedia import SocialMedia
from InstagramAPI import InstagramAPI


class Instagram(SocialMedia):
    def __init__(self, senero):
        self.senero = senero
        self.api = InstagramAPI(senero['instagram']['username'], senero['instagram']['password'])
        self.api.login()

        super(Instagram, self).__init__(senero)

    def get_relevant(self):
        all_relevant_items = []
        for tag in ['senero', 'monero']:
            feed_resp = self.api.get_hashtag_feed(tag)
            items = feed_resp.json()["items"]
            items = Instagram.filter_items(items)
            all_relevant_items.extend(items)
        Instagram.sort_items_by_likecount(all_relevant_items)
        return all_relevant_items

    def update_status(self, txt, post=None):
        if post is not None:
            self.api.comment(post['caption']['media_id'], txt)

    def logout(self):
        self.api.logout()

    @staticmethod
    def filter_items(items):
        items = list(filter(lambda item: not item["has_liked"], items))
        return items

    @staticmethod
    def sort_items_by_likecount(items):
        items.sort(key=lambda item: item["like_count"], reverse=True)
