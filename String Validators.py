



def is_alnum(s):
    for i in range(len(s)):
        if s[i].isalnum():
            return True
            break
    return False

def  is_alpha(s):
    for i in range(len(s)):
        if s[i].isalpha():
            return True
            break
    return False

def  is_digit(s):
    for i in range(len(s)):
        if s[i].isdigit():
            return True
            break
    return False

def is_lower(s):
    for i in range(len(s)):
        if s[i].islower():
            return True
            break
    return False

def is_upper(s):
    for i in range(len(s)):
        if s[i].isupper():
            return True
            break
    return False
            
        
    
            
    
s = input()
print(is_alnum(s))
print(is_alpha(s))
print(is_digit(s))
print(is_lower(s))
print(is_upper(s))