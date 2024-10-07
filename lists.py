#q1
def list_1(number1):
    return sum(number1)
my_list = [2, 3, 4, 5, 15, 1, 43, 20]
result1 = list_1(my_list)
print("the answer for q1 is : ", result1)
#q2
print("the answer for q2 is : ",max(my_list))
#q3
odd_list= [i for i in range(1200,2001,125)  if i%2 !=0 ]
print("the answer for q3 is : ",odd_list)
#q4
list_slice=odd_list[:5]
print("the answer for q4 is : ",list_slice)
