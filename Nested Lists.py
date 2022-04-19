




sort_list = []
for _ in range(int(input())):
    name = input()
    score = float(input())
    sort_list.append([name, score])

the_second_min = sorted(set([score for name,score in sort_list]))[1]



print('\n'.join(sorted([name for name,score in sort_list if score == the_second_min])))