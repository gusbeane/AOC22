import numpy as np

f = open('input.txt', 'r')

content = f.read()

content_split = content.split('\n')

def get_priority(letter):
    if letter.isupper():
        prior = ord(letter) - 64 + 26
    else:
        prior = ord(letter) - 96
    return prior

sum_priority = 0
for line in content_split[:-1]:
    firsthalf, secondhalf = line[:len(line)//2], line[len(line)//2:]

    common = list(set(firsthalf)&set(secondhalf))[0]
    prior = get_priority(common)

    sum_priority += prior

sum_priorityB = 0
for lineA, lineB, lineC in zip(content_split[::3], content_split[1::3], content_split[2::3]):
    common = list(set(lineA)&set(lineB)&set(lineC))[0]

    prior = get_priority(common)

    sum_priorityB += prior


print(sum_priority)
print(sum_priorityB)
# print(pts_partB)

