import numpy  
a,b = input().split()

lists = [] 

for _ in range(int(a)):
    n = list(map(int, input().split()))
    lists.append(n)
    
lists = numpy.array(lists)

print(numpy.mean(lists,axis=1))
print(numpy.var(lists,axis=0))
numpy.set_printoptions(legacy='1.13')
print(numpy.std(lists))