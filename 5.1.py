# Exercise 1: Write a program which repeatedly reads numbers until the user enters “done”.
# Once “done” is entered, print out the total, count, and average of the numbers. If the
# user enters anything other than a number, detect their mistake using try and except and
# print an error message and skip to the next number.

num = 0
total = 0.0
while True:
    enteredVal = input('Enter a number: ')
    if enteredVal == 'done':
        break
    try:
        fVal = float(enteredVal)
    except:
        print('Invalid input')
        continue
    # print(fVal) # for debugging purposes
    num = num + 1
    total = total + fVal
# print('Done')
print(total,  num, total / num)
