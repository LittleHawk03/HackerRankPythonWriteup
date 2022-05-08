import numpy

n, m, p = input().split()

lists1 = []
lists2 = []

for _ in range(int(n)):
    a = list(map(int, input().split()))
    lists1.append(a)

for _ in range(int(m)):
    b = list(map(int, input().split()))
    lists2.append(b)

matrix_arr1 = numpy.array(lists1)
matrix_arr2 = numpy.array(lists2)
 
print(numpy.concatenate((matrix_arr1,matrix_arr1)))


    