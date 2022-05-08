import numpy  


def arrays(arr):
    res = arr[::-1]
    return numpy.array(res,float)

arr = input().strip().split(' ')
result = arrays(arr)
print(result)

