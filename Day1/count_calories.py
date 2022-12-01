import numpy as np

f = open('input.txt', 'r')

content = f.read()

content_split = content.split('\n\n')

cal_list = []
for line in content_split:
    cal = 0
    line_split = line.split('\n')
    for treat in line_split:
        if treat != '':
            cal += float(treat)
    
    cal_list.append(cal)

cal_list_sorted = np.sort(cal_list)

print(cal_list_sorted[-1])
print(cal_list_sorted[-1]+cal_list_sorted[-2]+cal_list_sorted[-3])
