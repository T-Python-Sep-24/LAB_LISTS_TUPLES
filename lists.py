#q1
def list_1(number1):
    for x in (number1):
        print(x)
list_2=[1,2,3]
print("the answer for q1 is : ")
list_1(list_2)
#q2
print("the answer for q2 is : ",max(list_2))
#q3
odd_list= [i for i in range(1200,2001,125)  if i%2 !=0 ]
print("the answer for q3 is : ",odd_list)
#q4
list_slice=odd_list[:5]
print("the answer for q4 is : ",list_slice)
