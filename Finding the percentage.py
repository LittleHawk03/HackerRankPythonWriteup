


n = int(input())
student_mark = {}

for _ in range(n):
    name, *line = input().split() 
    scores = list(map(float, line))
    student_mark[name] = scores
    
name_sum = input()

print('{:.2f}'.format(sum(student_mark[name_sum])/3))