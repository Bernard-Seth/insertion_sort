import random

#allows user to create a set of numbers, at their desiered length
setSize = int(input('How many numbers are we sorting today?'))
#creates a random list of numbers between 0 and 999,999
numbers = random.sample(range(0, 999999), setSize)

def sort(arr, i, j):
    

#shows the original set of numbers
    print("Our set of numbers is " + str(numbers))

#if the set size is one, there is no need to sort, and is printed
    if setSize==1:
        print(str(numbers))

#sorts array numbers, starting at zero, using the set size.
sort(numbers, 0, setSize - 1)

print('The sorted set is')
for i in range(setSize):
    print(str(numbers[i]))