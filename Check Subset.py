

k = int(input())

for _ in range(k):
    n = int(input())
    s1 = set(map(int, input().split()))
    m = int(input())
    s2 = set(map(int, input().split()))
    print(s1.issubset(s2))  
            
        