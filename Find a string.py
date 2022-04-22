

import string
from tokenize import String


def count_substring(string, sub_string):
    string2 = str(string)
    sub_string2 = str(sub_string)
    
    lenStr = len(string2)
    lenSubStr = len(sub_string2)
    
    sum = 0
    
    for i in range(lenStr):
        print(string2[i:i+lenSubStr])
        if (string2[i:i+lenSubStr] == sub_string2):
    
            sum = sum + 1
    return sum        
    
    
    
    
    

string = input().strip()
sub_string = input().strip()
result = count_substring(string, sub_string)
print(result)
