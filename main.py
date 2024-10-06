list= [2, 3, 4, 5, 15, 1, 43, 20]
#task1
def sum_of_all(list):
    return sum(list)
print(sum_of_all(list))

#task2
def largest_number(list):
    return max(list)
print(largest_number(list))

#task3
odd_numbers= [n for n in range(1200, 2000, 125) if n%2 !=0]

print(odd_numbers)  

#task4
new_list= odd_numbers[:5]
print(new_list)