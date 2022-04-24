
def Binary(n):
    lists = []
    while n != 0 :
        r = n%2
        n = n // 2
        lists.append(str(r))
    lists = reversed(lists)
    return ''.join(lists)

def Octal(n):
    lists = []
    while n != 0 :
        r = n%8
        n = n // 8
        lists.append(str(r))
    lists = reversed(lists)
    return ''.join(lists)

def Hex(n): 
    return hex(n)[2:].upper()
    
    
def print_formatted(number):
    lenStr = len(Binary(number))
    
    for i in range(1,number + 1):
        print(str(i).rjust(lenStr,' '), end=' ')
        print(str(Octal(i)).rjust(lenStr,' '),end=' ')
        print(str(Hex(i)).rjust(lenStr,' '),end=' ')
        print(str(Binary(i)).rjust(lenStr,' '),end=' ')
        print("")
        

n = int(input())
print_formatted(n)
    