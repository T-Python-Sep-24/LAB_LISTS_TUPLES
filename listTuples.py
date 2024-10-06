'''## Given the following list : [2, 3, 4, 5, 15, 1, 43, 20]
### Q1: Write a function that takes a list as a parameter, and then returns  the sum  of all the items in that list.
### Q2: Write a function that takes a list as a parameter, and then returns the largest number from a list of numbers.
### Q3: Create an odd numbers list from the elements of a range from 1200 to 2000 with steps of 125, using [ List Comprehension ].
### Q4: use list slicing to get a new list from the previous list (odd numbers list) starting from the start to the 5th element in the list.'''


numbers = [2, 3, 4, 5, 15, 1, 43, 20]

#Function to return the sum of all items in a list
def sum_of_list(lst):
    return sum(lst)

#Function to return the largest number from a list
def largest_number(lst):
    return max(lst)

#Create an odd numbers list from the range 1200 to 2000 with steps of 125
odd_numbers = [num for num in range(1200, 2000, 125) if num % 2 != 0]

#Get a new list from the odd numbers list starting from the start to the 5th element
sliced_odd_numbers = odd_numbers[:5]

# Testing the functions and displaying results
print("Sum of the list:", sum_of_list(numbers))
print("Largest number in the list:", largest_number(numbers))
print("Odd numbers list:", odd_numbers)
print("Sliced odd numbers list:", sliced_odd_numbers)