#!/usr/bin/env python
# coding=utf-8

'''
Author: LonelyMarch
Date: 2020-12-27 12:39:41
LastEditors: LonelyMarch
LastEditTime: 2020-12-27 12:42:45
FilePath: /Python/demo/Narcissistic_numbers.py
version: 
Descripttion: 
'''

print('-----Narcissistic numbers-----')

for d in range(100,1000) :
    low_position = d % 10
    mid_position = d // 10 % 10
    high_position = d // 100
    e = low_position ** 3 + mid_position ** 3 + high_position ** 3
    if e == d :
        print(d)
