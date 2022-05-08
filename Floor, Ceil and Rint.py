
import numpy
numpy.set_printoptions(legacy='1.13')

lists = list(map(float, input().split()))


check_array = numpy.array(lists,float)

print(numpy.floor(check_array))
print(numpy.ceil(check_array))
print(numpy.rint(check_array))