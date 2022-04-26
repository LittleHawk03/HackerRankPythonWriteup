

n = int(input())
s = set(map(int, input().split()))

m = int(input())
for _ in range(m):
    a = input().split()
    if a[0] == 'pop':
        s.pop()
    elif a[0] == 'remove':
        arr = list(map(int, a[1]))
        s.remove(int(a[1]))
    elif a[0] ==  'discard':
        arr = list(map(int, a[1]))
        s.discard(int(a[1]))
print(sum(s))     