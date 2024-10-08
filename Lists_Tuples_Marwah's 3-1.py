#Given the following list : [2, 3, 4, 5, 15, 1, 43, 20]

#Q1: Write a function that takes a list as a parameter, and then returns the sum of all the items in that list.
def sum_of_list(numbers):
    return sum(numbers)
my_list = [2, 3, 4, 5, 15, 1, 43, 20]
result = sum_of_list(my_list)
print(f"The sum of the list is: {result}")

#Q2: Write a function that takes a list as a parameter, and then returns the largest number from a list of numbers.
def largest_number(numbers):
    return max(numbers)
my_list = [2, 3, 4, 5, 15, 1, 43, 20]
result = largest_number(my_list)
print(f"The largest number in the list is: {result}")

#Q3: Create an odd numbers list from the elements of a range from 1200 to 2000 with steps of 125, using [ List Comprehension ].
odd_numbers = [num for num in range(1200, 2001, 125) if num % 2 != 0]
print(f"The list of odd numbers is: {odd_numbers}")

#Q4: use list slicing to get a new list from the previous list (odd numbers list) starting from the start to the 5th element in the list.
odd_numbers = [num for num in range(1200, 2001, 125) if num % 2 != 0]
sliced_list = odd_numbers[:5]
print(f"The sliced list is: {sliced_list}")