#!/usr/bin/env python3
import tweepy
import sys
import os

AT = os.getenv('TW_AT')
AS = os.getenv('TW_AS')
CK = os.getenv('TW_CK')
CS = os.getenv('TW_CS')

auth = tweepy.OAuthHandler(CK, CS)
auth.set_access_token(AT, AS)
api = tweepy.API(auth)

status = api.update_status(status=sys.argv[1])

print('https://twitter.com/{}/status/{}'.format(status.user.screen_name, status.id))
