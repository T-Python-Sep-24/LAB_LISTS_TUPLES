listAllFun = [2,3,4,5,15,1,43,20]
 
def calculation (listAllFun:list):
    '''Calculates the sum of all elements in the provided list.

    Args:
        listAllFun (list): A list of integers to sum.

    Returns:
        int: The total sum of all elements in the list.
    ''' 
    total = 0 
    for items in listAllFun:
        total += items
    return total 

def check_large_number (listAllFun:list):
    '''Finds the largest number in the provided list.

    Args:
        listAllFun (list): A list of integers to find the largest number.

    Returns:
        int: The largest number in the list.
    '''
    va = 0 
    va=max(listAllFun)
    return va

def oddNumber():
    """Generates a global list of odd numbers from 1200 to 2000 with a step of 125 
    and then calls the list_slicing() function to further manipulate the list.

    This function uses a list comprehension to create the list and stores it in a global
    variable `listOddNumber`. It then prints this list and calls `list_slicing()` to slice 
    and print the first 5 elements.
    """
    global listOddNumber 
    listOddNumber=[odd for odd in range(1200,2000,125)
                    if odd % 2 == 1]
    print(f"This is by using  List Comprehension: {listOddNumber}")
    list_slicing()

def list_slicing():
    '''Slices the global list `listOddNumber` to get the first 5 elements and prints them.

    This function operates on the global variable `listOddNumber`, slices it, 
    and then prints the result.
    ''' 
    newList = []
    newList = listOddNumber [:5]
    print(f"This is new list: {newList}")



reslut = calculation(listAllFun) 
print(f"This is total: {reslut}")


vama = check_large_number(listAllFun)
print(f"This is the largest number from a list:{vama}")

oddNumber()