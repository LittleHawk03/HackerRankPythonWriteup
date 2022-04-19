
n = int(input())

lists = []

for _ in range(n):
    funt, *line = input().split()
    if funt  == 'insert':
        arr = list(map(int, line))
        lists.insert(arr[0], arr[1])
    elif funt == 'append':    
        arr = list(map(int, line))
        lists.append(arr[0])
    elif funt == 'remove':
        arr = list(map(int, line))
        lists.remove(arr[0])
    elif funt == 'sort':
        lists.sort()
    elif funt == 'reverse':
        lists.reverse()
    elif funt == 'pop':
        lists.pop()
    elif funt == 'print':
        print(lists)        