'''
Created on Feb 4, 2024

@author: rob.fenoglio
'''
'''
#lecture example

import re

hand = open ('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('From:', line):
        print(line)
'''

#lecture example

import re

hand = open ('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('^From:', line):
        print(line)
