from itertools import permutations

a ,b = input().split()

n = int(b)

perList = permutations(a,n)
perList = sorted(perList)

for n in perList:
    print(*[''.join(n)])