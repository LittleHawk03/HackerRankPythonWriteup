from itertools import combinations_with_replacement

a, b = input().split()

listCom = combinations_with_replacement(sorted(a), int(b))
listCom = sorted(listCom)
# print('\n'.join(sorted([n for n in a])))
for n in listCom:
    print(*[''.join(n)])
