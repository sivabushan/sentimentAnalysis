#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 14:04:17 2017

@author: siva
"""

import json
#import pandas as pd
#import matplotlib.pyplot as plt


tweets_data_path = 'twitter.txt'

tweets_data = []
tweets_file = open(tweets_data_path, "r")
for line in tweets_file:
    try:
        tweet = json.loads(line)
        tweets_data.append(tweet)
        print(tweet)
    except:
        continue
    
print(len(tweets_data))