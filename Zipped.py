
a , b = input().split()

lists = []

for _ in range(int(b)):
    l = map(float, input().split())
    lists.append(l)

for i in zip(*lists):
    print(sum(i)/int(b))
    
