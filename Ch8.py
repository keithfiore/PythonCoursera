# Lists and Functions
# A list is a sequence
# Lists are mutable

# Unlike strings, lists are mutable because you can change the order of items in a list
# or reassign an item in a list. When the bracket operator appears on the left side of an
# assignment, it identifies the element of the list that will be assigned.

fruit = 'Banana'
# fruit[0] = 'b'
print(fruit, '\n')

a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print(c)
print(len(c))

print('\n')

t = [9, 41, 12, 3, 74, 15]
print(t[2:4])

print('\n')

friends = ['Joseph', 'Glenn', 'Sally']
friends.sort()
print(friends[0]) # prints Glenn

print('\n')

numbers = [17, 123]
numbers[1] = 5
print(numbers, '\n')

# [17, 5] - the output of the print function
# The one-th element of numbers, which used to be 123, is now 5.


# Examples of different (data type) Lists
cheeses = ['Cheddar', 'Edam', 'Gouda']
numbers = [17, 123]
empty = []
print(cheeses, numbers, empty, '\n')


# functions ( max(), len(), etc. ) work with lists of strings and other types that can be comparable.
alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
         'w', 'x', 'y', 'z']
m = max(alpha)
print(m)
print(len(alpha),'\n')

# Traversing a list
# The most common way to traverse the elements of a list is with a for loop. The syntax is the same as for strings:
#
for cheese in cheeses:
     print(cheese, '\n')

# This works well if you only need to read the elements of the list. But if you want to write or update the elements,
# you need the indices. A common way to do that is to combine the functions range and len:

for i in range(len(numbers)):
     numbers[i] = numbers[i] * 2
     print(i)

print('\n')


# Slice Operator works with Lists
t = ['a', 'b', 'c', 'd', 'e', 'f']
print(t[1:3])
#['b', 'c']

print(t[:4])
# ['a', 'b', 'c', 'd']
print(t[3:])
# ['d', 'e', 'f']

# split() breaks a string into parts and produces a list of strings

abc = "with these words"
print(abc, '\n')
stuff = abc.split()
print(stuff, '\n')
print(len(stuff))
print('\n')
for w in stuff:
    print(w)

print('\n')

line = 'first;second;third'
thing = line.split()
print(thing, '\n')
print (len(thing)) # the semicolons are not delimiting

# How can you separate the words?
thing = line.split(';') # You can specify the delimiter character to use in split()
print(thing, '\n')
# Now the words are separated with the semicolon delimiter
print(len(thing))

print('\n')

fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From '):
        continue # skips everything BUT From
    words = line.split()
    # From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
    print(words[1]) # Index of the text in file... 0 is From, 1 is email, 2 is day...

print('\n')
