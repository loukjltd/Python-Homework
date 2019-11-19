# Exercise 14-02
'''
Student Name: Sean
ID: 201810701580042
Class: Network 182
'''

f = open("C:/PycharmProjects/Python Homework/Exercise14/my_text2.txt", "r")
s = 0

for x in f.readlines():
    s += int(x)

print('Sum: ' + str(s))
