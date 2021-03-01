# from Py4e.com - https://www.py4e.com/html3/07-files

fhand = open('mbox-short.txt')
count = 0
for line in fhand:
    count = count + 1
print('Line Count:', count)

# This will output, Line Count: 1910
print('\n \n')

fhand = open('mbox-short.txt')
count = 0
for line in fhand:
    if line.startswith('From:'):
        print(line)

# This will output all email addresses from file - Extra Spaces, though
# From: stephen.marquard@uct.ac.za
#
# From: louis@media.berkeley.edu
#
# From: zqian@umich.edu

fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip() #use the function rstrip() to remove extra spaces
    if line.startswith('From:'):
        print(line)

# No more extra spaces between email addresses
# From: stephen.marquard@uct.ac.za
# From: louis@media.berkeley.edu
# From: zqian@umich.edu
print('\n \n')

fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    # Skip 'uninteresting lines'
    if not line.startswith('From:'):
        continue
    # Process our 'interesting' line
    print(line)

# Try/Except & Open
fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()
count = 0
for line in fhand:
    if line.startswith('Subject:'):
        count = count + 1
print('There were', count, 'subject lines in', fname)
