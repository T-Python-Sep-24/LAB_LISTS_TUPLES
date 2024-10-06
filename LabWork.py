#The list for our operations
numberslist: list[int] = [2, 3, 4, 5, 15, 1, 43, 20]

#Q1 function:
def sumOfNumbers (numbers: list[int]) -> int:
    '''
    This is a function that takes a list as a parameter, and then returns the sum of all the items in that list.
    Args:
        numbers(list[int]): list of all numbers to be summed
    Returns:
        Sum of all numbers in the list
    '''
    sum: int = 0
    for n in numbers:
        sum += n

    return sum
#Print results
print(sumOfNumbers(numberslist))

#Q2 function:
def largestNumber(numbers: list[int]) -> int:
    '''
    This is a function that takes a list as a parameter, and then returns the largest number from a list of numbers.
    Args:
        numbers(list[int]): list of all numbers to be summed
    Returns:
        Largest number in the list

    '''
    largestN: int = 0

    for n in numbers:
        if n > largestN:
            largestN = n

    return largestN
#Print results
print(largestNumber(numberslist))

#Q3 answer:
#Odd numbers list from the elements of a range from 1200 to 2000 with steps of 125
oddNumbers: list[int] = [n for n in range(1200, 2001, 125) if n % 2 != 0]
print(oddNumbers)

#Q4 answer:
#Sliced list form the first element in the oddNumbers list to the 5th element
slicedList: list[int] = oddNumbers[:5]
print(slicedList)
