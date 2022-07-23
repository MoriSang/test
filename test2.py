"""
Created on 2022-7-23 19:12:08
@author: Keithen
"""

import re

f = open('long_text.txt', 'r', encoding = "utf-8")
content = f.readlines()
content = ''.join(content).split("\n")
f.close()

print('{')
print('\t\'name\': \'{}\','.format(content[0]))
print('\t\'lei\': \'{}\','.format(content[1]))
print('\t\'sub_fund\': [{')
sublist = content[2:]
for i in sublist:
    if i.find('.') != -1:
        print(']\n\t}, {')
        i = re.sub('[1-9.]', '', i)
        print('\t\t\'title\': \'{}\','.format(i[1:]))
        print('\t\t\'isin\': [', end="")
    else:
        print('\'{}\', '.format(i), end="")
print(']\n\t}]\n}')
