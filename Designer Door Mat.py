

def door_Mat(a, b):
    
    c = ".|."
    d = (b-1)//2
    e = (a-1)//2
    
    for i in range(e):
        print((c*i).rjust(d-1,'-') + c + (c*i).ljust(d-1,'-'))    
        
    print('WELCOME'.center(b,'-'))
    
    for i in range(e):
        print((c*(e - i - 1)).rjust(d -1,'-') + c + (c*(e - i - 1)).ljust(d -1,'-'))
        


lists = list(map(int, input().split()))
a = int(lists[0])
b = int(lists[1])

door_Mat(a,b)