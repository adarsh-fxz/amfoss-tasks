#!/bin/python3

import sys


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    n -= 1
    n3 = n // 3
    n5 = n // 5
    n15 = n // 15
    
    s3 = (n3 * 3 * (n3 + 1) // 2)
    s5 = (n5 * 5 * (n5 + 1) // 2)
    s15 = (n15 * 15 * (n15 + 1) // 2)
    
    print(s3 + s5 - s15)