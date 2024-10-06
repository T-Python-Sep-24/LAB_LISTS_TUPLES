
def sumItems(items): #q1:returns the sum
   return sum(items)

def largestItems(items):#q2: returns the largest number 
   return  max(items)


items = [2, 3, 4, 5, 15, 1, 43, 20]
print("sum : ",sumItems(items))
print("largest number : ",largestItems(items))



oddNumbers = list(num for num in range(1200,2000,125) if num % 2 != 0) #q3: range from 1200 to 2000 with step: 125
print("odd numbers from 1200 to 2000 with step 125 : ",oddNumbers)

slicing = oddNumbers[ : 5]#q4: starting from the start to the 5th element but the new list has three element
print("first 5 elements of the odd numbers list : ",slicing)





   


