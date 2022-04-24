from itertools import product



l1 = list(map(int, input().split()))
l2 = list(map(int, input().split()))


print(*list(product(l1,l2)))    