#!/bin/python3

import sys


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    a, b = 1, 2
    sum = 0
    while (b < n):
        if b % 2 == 0:
            sum += b
            
        temp = a + b
        a = b
        b = temp
        
    print(sum)