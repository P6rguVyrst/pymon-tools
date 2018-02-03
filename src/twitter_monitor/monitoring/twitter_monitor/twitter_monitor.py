# -*- coding: utf-8 -*-

"""Main module."""
from twython import Twython
import json
import csv

class Monitor:

    def __init__(self, config):
        #TODO: Define secrets as private variables
        consumer_key = None
        consumer_secret = None
        access_token = None
        access_token_secret = None
        self.twitter = Twython(
            consumer_key,
            consumer_secret,
            access_token,
            access_token_secret)

    def run(self, key, date_from, date_to, operation='search', **kwargs):

        options = {
            'search': search,

        }

        return options[operation]()

    def search(self):
        tweetsXiteration = 100
        countTweets = len(response['statuses']);
        response = twitter.search(
            q=keyword,
            count=tweetsXiteration,
            since=dateFrom,
            until=dateTo,
            result_type='mixed')

        return countTweets
