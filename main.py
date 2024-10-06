# LAB_LISTS_TUPLES



        ## Given the following list : [2, 3, 4, 5, 15, 1, 43, 20]
### Q1
def sum_of_list_items(mylist:list)-> float:
    result=0
    for i in mylist:
        result+=i
    return result    



### Q2

def find_largest_number(mylist)-> int:
    largest_number=0
    for i in mylist:
        if i>largest_number:
            largest_number=i
    return largest_number        




print(sum_of_list_items([2, 3, 4, 5, 15, 1, 43, 20]))
print(find_largest_number([2, 3, 4, 5, 15, 1, 43, 20]))

### Q3

odd_list=[x for x in range(1200,2001,125) if x%2!=0 ]
print(odd_list)


### Q4

new_list=odd_list[:6]
print(new_list)

