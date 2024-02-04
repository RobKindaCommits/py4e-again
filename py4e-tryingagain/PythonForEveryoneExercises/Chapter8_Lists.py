'''
Created on Feb 4, 2024

@author: rob.fenoglio
'''
'''
#lecture scratch work
friends = ['Joseph', 'Glenn', 'Sally']
print(friends)
friends[1] = 'Jeremy'
print(friends)
for i in range(len(friends)):
    print(friends[i],i)

'''
'''
#Assignment 8.4

fh = open('romeo.txt')
compendium = []
for line in fh:
    cleanline=line.rstrip()
    splitlist=cleanline.split()
#    print(splitlist)
    for word in splitlist:
        if word not in compendium:
            compendium.append(word)

compendium.sort()
print(compendium)
'''

#Assignment 8.5
fh=open('mbox-short.txt')
instancecount = 0
for line in fh:
    if line.startswith('From '):
        linelist=line.split()
        print(linelist[1])
        instancecount=instancecount+1
print('There were', instancecount, 'lines in the file with From as the first word')
