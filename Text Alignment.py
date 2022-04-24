

s = int(input())
h = 'H'



for i in range(s):
    print((h*i).rjust(s-1) + h + (h*i).ljust(s-1))

for i in range(s + 1):
    print((h * s).center(s*2) + (h*s).center(s*6))
    
for i in range((s+1)//2):
    print((h*s*5).center(s*6))
    
for i in range(s + 1):
    print((h * s).center(s*2) + (h*s).center(s*6))
    
for i in range(s):
   print(((h*(s-i-1)).rjust(s)+h+(h*(s-i-1)).ljust(s)).rjust(s*6))