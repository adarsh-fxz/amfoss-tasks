#!/bin/python3

import sys

def gcd(a, b):
    if b:
        return gcd(b, a % b)
    else:
        return a

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    pro = 1
    for num in range(2, n+1):
        pro *= num // gcd(pro, num)
    print(pro)