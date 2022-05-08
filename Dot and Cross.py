import numpy  

a = int(input())


    
matrix_array = numpy.array([input().split() for _ in range(a)],int)
matrix_array1 = numpy.array([input().split() for _ in range(a)],int)

print(numpy.dot(matrix_array,matrix_array1))