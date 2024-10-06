#Q1: Write a function that takes a list as a parameter, and then returns the sum of all the items in that list.

# Function to calculate the sum of all items in a list
def listSum(n_list):
    total = 0  # Initialize total to zero
    for i in n_list:  # Iterate through each item in the list
        total += i  # Add the item to total
    return total  # Return the final total

# Given list
n_list = [2, 3, 4, 5, 15, 1, 43, 20]   
# Call the function and print the sum of the list
print("The sum of the list is:", listSum(n_list))
