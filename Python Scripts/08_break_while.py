# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 12:37:10 2020

@author: CEC
"""

while True:
    x=input("enter a number to count to: ")
    if x=='q' or x=='quit':
        break
    x=int(x)
    y=1
    while True:
        print(y)
        y=y+1
        if y>x:
            break