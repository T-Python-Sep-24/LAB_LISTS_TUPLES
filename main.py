#Q1
def sum_list(numbers):
    return sum(numbers)

# Example usage:
x = [2,3,4,5,15,43,20]
result = sum_list(x)
print(result)

#Q2
def largeast_in_list(numbers):
    return max(numbers)

result_of_max = largeast_in_list(x)
print(result_of_max)

#Q3
odd_numbers = [n for n in range(1200, 2000, 125) if n % 2 != 0]
print(odd_numbers)

#Q4
sliced_list = odd_numbers[:5]
print(sliced_list)

