
from collections import OrderedDict

n = int(input())

lists = OrderedDict()

for _ in range(n):
    item = input().split()
    itemPrice = int(item[-1])
    itemName = ' '.join(item[:-1])
    if lists.get(itemName):
       lists[itemName] += itemPrice
    else :
        lists[itemName] = itemPrice

    
for i in lists.keys():
    print(i, lists[i])
    
     