mylist = [2, 3, 4, 5, 15, 1, 43, 20]

def sumOfList(items: list) -> int:
    """
    Calculate the sum of all the items

    Args:
        items (list): list of items

    Returns:
        int: sum of all the items
    """
    sum = 0
    for item in items:
        sum += item

    return sum

print(f"Sum: {sumOfList(mylist)}")


def largestNumber(items: list) -> int:
    """
    Takes a list and return the largest number

    Args:
        items (list): list of items

    Returns:
        int: the largest number of the list
    """

    max = 0
    for item in items:
        if item > max:
            max = item
    return max

print(f"Max: {largestNumber(mylist)}")


''' 
Create an odd numbers list from the elements of a range
from 1200 to 2000 with steps of 125, using [ List Comprehension ]
'''
oddList = [x for x in range(1200, 2001, 125) if x % 2 != 0]
print(f"Odd Number List: {oddList}")

'''
use list slicing to get a new list from the previous list (odd numbers list) 
starting from the start to the 5th element in the list.
'''
newList = oddList[:6]
print(f"New List: {newList}")