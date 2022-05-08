import numpy  

a,b = input().split()

lists = [] 

for _ in range(int(a)):
    n = list(map(int, input().split()))
    lists.append(n)

matrix_array = numpy.array(lists)

print(numpy.transpose(matrix_array))
print(matrix_array.flatten())
