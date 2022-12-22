import numpy as np

f = open('input.txt', 'r')

content = f.read()

content_split = content.split('\n')

sum = 0
sum_at_all = 0
for line in content_split[:-1]:
    firstp, secondp = line.split(',')
    firstp0, firstp1 = firstp.split('-')
    secondp0, secondp1 = secondp.split('-')

    firstp0, firstp1 = int(firstp0), int(firstp1)
    secondp0, secondp1 = int(secondp0), int(secondp1)

    first_in_second = firstp0 >= secondp0 and firstp1 <= secondp1
    second_in_first = secondp0 >= firstp0 and secondp1 <= firstp1

    if first_in_second or second_in_first:
        sum += 1
    
    firstp0_bool = firstp0 >= secondp0 and firstp0 <= secondp1
    firstp1_bool = firstp1 >= secondp0 and firstp1 <= secondp1

    secondp0_bool = secondp0 >= firstp0 and secondp0 <= firstp1
    secondp1_bool = secondp1 >= firstp0 and secondp1 <= firstp1
    
    first_bool = firstp0_bool or firstp1_bool
    second_bool = secondp0_bool or secondp1_bool

    if first_bool or second_bool:
        sum_at_all += 1

print(sum)
print(sum_at_all)
# print(sum_priorityB)
# print(pts_partB)

