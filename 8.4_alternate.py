fname = input("Enter file name: ")
fh = open(fname)
lst = list()  # list for the desired output
print(lst, '\n')
for line in fh:  # to read every line of file romeo.txt
    word = line.rstrip().split()  # to eliminate the unwanted blanks and turn the line into a list of words
    for words in word:  # check every word in words
        if words in lst:
            continue  # if words are repeated
        else:
            lst.append(words)  # append else if words is not in the list
lst.sort()
print(lst) # sort the list (de-indent indicates that you sort when the loop ends)

