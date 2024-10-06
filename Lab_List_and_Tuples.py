def sum_of_list(lst):
    return sum(lst)

def largest_number(lst):
    return max(lst)

def odd_numbers_list():
    return [x for x in range(1200, 2000, 125) if x % 2 != 0]

# Ex
numbers = [2, 3, 4, 5, 15, 1, 43, 20]

# Q1: Sum of all items
print("Sum:", sum_of_list(numbers))  # Output: 93

# Q2: Largest number
print("Largest Number:", largest_number(numbers))  # Output: 43

# Q3: Create odd numbers list
odd_numbers = odd_numbers_list()
print("Odd Numbers List:", odd_numbers)

# Q4: List slicing
sliced_odd_numbers = odd_numbers[:5]  # Get the first 5 elements
print("Sliced Odd Numbers List:", sliced_odd_numbers)
