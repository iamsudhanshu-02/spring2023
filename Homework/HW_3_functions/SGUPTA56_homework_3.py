#!/usr/bin/env python
# coding: utf-8
import math 
import csv

def findChar(a,b):
    try:
        assert type(a)==str
        assert type(b)==int
        result = a[b-1]
        return result
    except (AttributeError, TypeError):
        raise AssertionError('Input variables should be strings')

# print(findChar("abcdef",3))

def doMath(c,d,e):
    x = e.count(d)
    result = (c**3) + math.floor(c/0.65) +  (x)
    return result
    
# print(doMath(3,'w',[1,'w','w',9]))

def fileInfo(f: str) -> list:
    with open(f) as csv_file:
        csv_reader = csv.reader(csv_file)
        rows = sum(1 for row in csv_reader)
        csv_file.seek(0)
        cols = len(next(csv_reader))
    return [rows, cols]

# filepath = './practice.csv' 
# print(fileInfo(filepath))




