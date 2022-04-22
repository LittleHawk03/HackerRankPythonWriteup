
from curses.ascii import islower


def swap_case(s):
    lists = list(s)
    for i in range(len(lists)):
        if lists[i].islower():
           lists[i] = lists[i].upper()
        elif lists[i].isupper():
           lists[i] = lists[i].lower()
    return ''.join(lists)    
    
    
    

s = input()
result = swap_case(s)
print(result)
