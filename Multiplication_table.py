#!/usr/bin/env python
# coding=utf-8

'''
Author: LonelyMarch
Date: 2020-12-27 12:40:19
LastEditors: LonelyMarch
LastEditTime: 2020-12-27 12:43:06
FilePath: /Python/demo/Multiplication_table.py
version: 
Descripttion: 
'''

print('----------Multiplication_table----------')

for row in range(1,10):
    for column in range(1,row + 1) :
        print(row,'*',column,'=',row*column,end='\t')
    print()
