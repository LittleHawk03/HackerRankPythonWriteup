

k = int(input())
l = sorted(map(int, input().split()))

for i in range(len(l)):
    if(i != len(l)-1):
        if(l[i]!=l[i-1] and l[i]!=l[i+1]):
            print(l[i])
            break;
    else:
        print(l[i])
        