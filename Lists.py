def getSum(list:list):
    sum = 0
    for item in list:
        sum += item
    
    return sum

def getMax(list:list):
    max = list[0]
    for num in list:
        if num > max:
            max = num
    return max

theList = [2, 3, 4, 5, 15, 1, 43, 20]
print()
print('The Orginal List:', theList)
print()

listSum = getSum(theList)
print('The sum of list items =', listSum)
maxNumber = getMax(theList)
print('The largest number in the list =', maxNumber)

print()
oddList = [x for x in range(1200, 2000, 125) if x % 2 != 0]
print('The Odd List:', oddList)

print()
newOddList = oddList[:5]
print('The New Odd List with slicing [:5]:', newOddList)

print()
oddList2 = [x for x in range(1200, 2000, 25) if x % 2 != 0]
print('The Odd List with 25 steps:', oddList2)

print()
newOddStepList = oddList2[:5]
print('The first 5 numbers in a List from the 25 step list:', newOddStepList)
print()

