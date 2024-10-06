
theList = [2,33,32,122,3,4,5,15,1,43,20]

# Q1 (sum(theList))
def sumOfList(a_list):
    the_sum = 0
    for i in a_list:
        the_sum += i
    return the_sum


print("The sum of the list is:", sumOfList(theList))


# Q2 (max(theList))
def maxOfList(a_list):
    temp = 0
    for n in a_list:
        if n > temp:
            temp = n
    return temp


print("The largest number in the list is:", maxOfList(theList))

# Q3 (List Comprehension)
oddList = [x for x in range(1200, 2000, 125) if x % 2 != 0]
print(oddList)

# Q4 (Slicing the above list)
newList = oddList[:5]
print(newList)
