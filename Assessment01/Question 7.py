# Assessment 1 Question 7
'''
Student Name: Sean
ID: 201810701580042
Class: Network 182
'''

list1 = []
list2 = []
same = 0
insert1 = input('Enter the first line of numbers separated by commas: ')
insert2 = input('Enter the second line of numbers separated by commas: ')
for i in insert1.split(','):
    list1.append(float(i))

for j in insert2.split(','):
    list2.append(float(j))

for m in list1:
    for n in list2:
        if m == n:
            same += 1

print('There are ' + str(same) + ' numbers that are in both lists')
