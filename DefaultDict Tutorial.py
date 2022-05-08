

from collections import defaultdict
from collections import defaultdict

n, m = map(int, input().split())

lists = defaultdict(list)

for i in range(1, n+1):
    lists[input()].append(i)

for i in range(1, m+1):
    key = input()
    if len(lists[key]) > 0:
        print(' '.join(str(c) for c in lists[key]))
    else:
        print('-1')
        
    
    
