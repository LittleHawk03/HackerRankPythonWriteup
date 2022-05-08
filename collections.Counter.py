

import collections

from collections import Counter

n = int(input())
arr = list(map(int, input().split()))

m = int(input())
purchase = 0

for _ in range(m):
    s = input().split()
    if arr.count(int(s[0])) != 0:
        purchase = purchase + int(s[1])
        arr.remove(int(s[0]))
        
print(purchase)