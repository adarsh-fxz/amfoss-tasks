#!/bin/python3

import sys

def lpf(n):
    lf = -1
    
    c = 2
    while c * c <= n:
        if n % c == 0:
            while n % c == 0:
                n = n // c
            lf = c
        c += 1
    
    if n > 1:
        lf = n
    
    return lf

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(lpf(n))
    