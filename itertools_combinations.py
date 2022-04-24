
from itertools import combinations

a, b = input().split()


for i in range(1, int(b) + 1):
    listCom = combinations(sorted(a), int(i))
    listCom = sorted(listCom)
    # print('\n'.join(sorted([n for n in a])))
    for n in listCom:
        print(*[''.join(n)])
    

