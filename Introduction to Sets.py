
def average(arr):
    arr2 = list(set(arr))
    return "{:.3f}".format(sum(arr2)/len(arr2))
    



n = int(input())
arr = list(map(int, input().split()))
print(average(arr))