#!/usr/bin/env python
# coding=utf-8

'''
Author: LonelyMarch
Date: 2020-12-27 12:37:08
LastEditors: LonelyMarch
LastEditTime: 2020-12-27 12:43:13
FilePath: /Python/demo/Fibonacci_sequence.py
version: 
Descripttion: 
'''

print('----------Fibonacci_sequence----------')

a = 1
b = 1

while b < 100:
    a, b = b, a + b
    print(b)
