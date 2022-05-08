
import re

n = int(input())

for _ in range(n):
    try:
        re.compile(input())
        output = True
    except re.error :
        output = False
    print(output)
    
    