# Use words.txt as the file name
# fname = input("Enter file name: ")
# fh = open(fname)

# fname = input('Enter the file name: ')
# fhand = open(fname)
# count = 0
# for line in fhand:
#    if line.startswith('Subject:'):
#        count = count + 1
# print('There were', count, 'subject lines in', fname)
# Use words.txt as the file name
fname = input("Enter file name: ")
try:
	fh = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()
words = fh.read().strip()
print(words.upper())