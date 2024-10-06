def sum_list(list:list)->int:
    sum=0
    for number in list:
        sum +=number
    return sum
def maximum_num(list:list)->int:
    max=list[0]
    for number in list:
        if number>max:
            max=number
    return max


List=[2, 3, 4, 5, 15, 1, 43, 20]
print(sum_list(List))
print(maximum_num(List))

odd_numbers=[number for number in range(1200,2000,125)if number%2 !=0]
print(odd_numbers)
new_oddlist=odd_numbers[:6]
print(new_oddlist)