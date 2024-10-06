# LAB_LISTS_TUPLES

## Given the following list : [2, 3, 4, 5, 15, 1, 43, 20]
list_a = [2, 3, 4, 5, 15, 1, 43, 20]

### Q1: Write a function that takes a list as a parameter, and then returns  the sum  of all the items in that list.
print(f'the sum  of all the items in that list: {sum(list_a)}')

### Q2: Write a function that takes a list as a parameter, and then returns the largest number from a list of numbers.
print(f'the largest number from a list of numbers: {max(list_a)}')
### Q3: Create an odd numbers list from the elements of a range from 1200 to 2000 with steps of 125, using [ List Comprehension ].
odd_numbers = [numbers for numbers in range(1200,2000,125) if not numbers%2 == 0]
print(f'odd numbers list: {odd_numbers}') 
### Q4: use list slicing to get a new list from the previous list (odd numbers list) starting from the start to the 5th element in the list.
list_slicing = odd_numbers
print(f'starting from the start to the 5th element in the list: {list_slicing[:5]}')