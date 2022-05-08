cube = lambda x:x**3


def fibonacci(n):
    lists = [0,1]
    for i in range(2,n):
        a = lists[i-1] + lists[i-2]
        lists.append(a)
    return lists[:n]
    
    
n = int(input())
print(list(map(cube, fibonacci(n))))
