
s = set(map(int, input().split()))
n = int(input())
check_sup = True

for _ in range(n):
    s2 = set(map(int, input().split()))
    if not s2.issubset(s):
        check_sup = False
    if len(s2) >= len(s):
        check_sup = False
        
print(check_sup)
            

