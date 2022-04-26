



n = int(input())
a = set(map(int, input().split()))
m = int(input())
b = set(map(int, input().split()))


e = sorted(list(a.difference(b)) + list(b.difference(a)))
for n in e:
    print(n)
    
