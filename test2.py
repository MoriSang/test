"""
Created on 2022-7-23 19:12:08
@author: Keithen
"""

import re

f = open('long_text.txt', 'r', encoding="utf-8")
content = f.readlines()
content = ''.join(content).split("\n")
f.close()

print('{')
print('\t\'name\': \'{}\','.format(content[0]))
print('\t\'lei\': \'{}\','.format(content[1]))
print('\t\'sub_fund\': [', end="")
sublist = content[2:]
for i in range(len(sublist)):
    if sublist[i].find('.') != -1:
        sublist[i] = re.sub('[1-9.]', '', sublist[i])
        print('{'+'\n\t\t\'title\': \'{}\','.format(sublist[i][1:]))
        print('\t\t\'isin\': [', end="")
    else:
        print('\'{}\''.format(sublist[i]), end="")
        if i+1 < len(sublist) and sublist[i+1][0] == 'L':
            print(', ', end="")
        elif i+1 == len(sublist):
            print(']\n\t}]\n}')
        else:
            print(']\n\t}, ', end="")

