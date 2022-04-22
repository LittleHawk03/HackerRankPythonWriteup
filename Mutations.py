




def mutate_string(string, position, character):
    return string[:int(position)] + str(character) + string[(int(position) +1):]




s = input()
i, c = input().split()
s_new = mutate_string(s, int(i), c)
print(s_new)
