def sum_of_list(list):
    return sum(list)

list_num = [2, 3, 4, 5, 15, 1, 43, 20]
print(sum_of_list(list_num))

def max_of_list(list):
    return max(list)


print(max_of_list(list_num))




def odd_num():
    return [x for x in range(1200, 2000, 125) if x % 2 == 1]


odd_num_list = odd_num()
print(odd_num_list)


print(odd_num_list[:5])
