
from  collections import namedtuple

n = int(input())
col = ','.join(input().split())
Student = namedtuple('student',col)

sum = 0
for i in range(n):
    row = input().split()
    student = Student(*row)
    sum = sum + int(student.MARKS)

print(sum/n)    

