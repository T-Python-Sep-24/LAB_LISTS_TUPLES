#Q2: Write a function that takes a list as a parameter, and then returns the largest number from a list of numbers.

# Function to find the largest number in a list
def listMax(list_num):
    largest = list_num[0]  # Start with the first number as the largest
    for n in list_num:  # Iterate through each number in the list
        if n > largest:  # If the current number is greater than the largest found
            largest = n  # Update largest to the current number
    return largest  # Return the largest number found

# Given list
n_list = [2, 3, 4, 5, 15, 1, 43, 20]
# Call the function and print the largest number in the list
print("The Largest number is:", listMax(n_list))
