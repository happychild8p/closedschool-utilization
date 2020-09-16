#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  9 20:37:24 2020
@Hasn't completed
@author: 남보은 안한성 양희동 이지연
@Usage: Closed School Utilization Project
    - Apply tf-idf algorithm on news articles for credibility
"""
from math import log

def tf(t, d):
    ## Term-Frequency
    # t is term in document
    # d is document
    return d.count(t)

def idf(t, dlist):
    ## d is document  (dlist is list of total documents)
    df = 0 ##number of doc contains term
    for d in dlist:
        if t in d:
            df = df + 1
    numerator = len(dlist)
    denominator = 1 + df
    
    return log(numerator/denominator)

def tfidf(t, d, dlist):
    ### result is count of 
    return tf(t, d) * idf(t, dlist)
