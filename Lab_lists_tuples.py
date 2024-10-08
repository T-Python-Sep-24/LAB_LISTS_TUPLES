'''
Given the following list : [2, 3, 4, 5, 15, 1, 43, 20]
Q1: Write a function that takes a list as a parameter, and then returns the sum of all the items in that list.
'''
list_lab =[2, 3, 4, 5, 15, 1, 43, 20]
def fun_list(l)-> int:
    return sum(l)
print(fun_list(list_lab))
'''
Q2: Write a function that takes a list as a parameter, and then returns the largest number from a list of numbers.
'''
print("-"*100)

def number_list(n)->int:
    for n in list_lab:
        if list_lab:
           list_lab.sort()
    return n
print(number_list(0))

print("-"*100)
'''
Q3: Create an odd numbers list from the elements of a range from 1200 to 2000 with steps of 125, using [ List Comprehension ].
'''
odd_numbers=[numbers for numbers in range(1200,2000,125)if numbers % 2 != 0]
print(odd_numbers)

print("-"*100)
'''
Q4: use list slicing to get a new list from the previous list (odd numbers list) starting from the start to the 5th element in the list.
'''
backup_listOdd=odd_numbers[0:5]
print(backup_listOdd)