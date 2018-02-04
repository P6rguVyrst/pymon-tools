# -*- coding: utf-8 -*-

"""Main module."""
from twython import Twython
import json
import csv

class Monitor:

    def __init__(self, config):

        #TODO: Define secrets as private variables
        consumer_key = config['consumer_key']
        consumer_secret = config['consumer_secret']
        access_token = config['access_token']
        access_token_secret = config['access_token_secret']

        self.max_tweets = config.get('max_tweets', 100)
        self.twitter = Twython(
            consumer_key,
            consumer_secret,
            access_token,
            access_token_secret)

    def run(self, key, date_from, date_to, operation='search', **kwargs):

        options = {
            'search': self.search,

        }

        return options[operation](
            key=key,
            date_from=date_from,
            date_to=date_to,
        )

    def search(self, **kwargs):
        keyword=kwargs['key']
        date_from=kwargs['date_from']
        date_to=kwargs['date_to']

        response = self.twitter.search(
            q=keyword,
            count=self.max_tweets,
            since=date_from,
            until=date_to,
            result_type='mixed')
        countTweets = len(response['statuses'])
        return countTweets



