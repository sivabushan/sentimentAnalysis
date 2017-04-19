#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 12:05:35 2017

@author: siva
"""

import tweepy
import datetime
#import xlsxwriter
import sys

# credentials from https://apps.twitter.com/
consumerKey = "bpdsWVZ0KrA3Ae3yu6Te0yicr"
consumerSecret = "74nbXsTkHUnEN75CI3LytMwd2aAABpzqH22boNmtJBHva5RN4H"
accessToken = "142980981-4f95Lx897pPu9TWV3gsM8OBpxopbd93e8Jayjjox"
accessTokenSecret = "skfsV7rREgguYo7DYLZQYUDwadxTwIudLvSCt3rd6gnBA"

auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
auth.set_access_token(accessToken, accessTokenSecret)

api = tweepy.API(auth)

username = "sivabushan"
startDate = datetime.datetime(2010, 6, 1, 0, 0, 0)
endDate =   datetime.datetime(2017, 1, 1, 0, 0, 0)

tweets = []
tmpTweets = api.user_timeline(username)
for tweet in tmpTweets:
    if tweet.created_at < endDate and tweet.created_at > startDate:
        tweets.append(tweet)
        print(tweet.text)
        

while (tmpTweets[-1].created_at > startDate):
    print("Last Tweet @", tmpTweets[-1].created_at, " - fetching some more")
    tmpTweets = api.user_timeline(username, max_id = tmpTweets[-1].id)
    for tweet in tmpTweets:
        if tweet.created_at < endDate and tweet.created_at > startDate:
            tweets.append(tweet)
            

#workbook = xlsxwriter.Workbook(username + ".xlsx")
#worksheet = workbook.add_worksheet()
#row = 0
#for tweet in tweets:
#    worksheet.write_string(row, 0, str(tweet.id))
#    worksheet.write_string(row, 1, str(tweet.created_at))
#    worksheet.write(row, 2, tweet.text)
#    worksheet.write_string(row, 3, str(tweet.in_reply_to_status_id))
#    row += 1
#
#workbook.close()
#print("Excel file ready")