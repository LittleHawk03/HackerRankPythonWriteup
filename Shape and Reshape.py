import numpy  


def arrays(arr):
    shape_array = numpy.array(arr,int)
    shape_array.shape = (3,3)
    return shape_array

arr = input().strip().split(' ')
result = arrays(arr)
print(result)

