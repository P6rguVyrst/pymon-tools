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
        self.twitter = Twython(
            consumer_key,
            consumer_secret,
            access_token,
            access_token_secret)

    def run(self, operation='search', **kwargs):
        options = {
            'search': self.search,

        }
        return options[operation](**kwargs)

    def search(self, **kwargs):
        response = self.twitter.search(
            q=kwargs.get('key'),
            count=kwargs.get('max_tweets', 100),
            since=kwargs.get('date_from'),
            until=kwargs.get('date_to'),
            result_type=kwargs.get('result_type', 'mixed')
        )
        countTweets = len(response['statuses'])
        return countTweets



