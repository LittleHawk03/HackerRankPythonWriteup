

n = int(input())
s = set(map(int, input().split()))

m = int(input())

for _ in range(m):
    a = input().split()
    r = set(map(int, input().split()))
    if a[0] == 'intersection_update':
       s.intersection_update(r)
    elif a[0] == 'update':
        s.update(r)
    elif a[0] == 'symmetric_difference_update':
        s.symmetric_difference_update(r)
    else:
        s.difference_update(r)
print(sum(s))
        
         
    