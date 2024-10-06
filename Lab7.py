#Lab 7
#numbers= [2, 3, 4, 5, 15, 1, 43, 20]

#Answer Q1
def my_sumList(numbers: list):
    result = sum(numbers)
    return result

my_final_result = my_sumList([2, 3, 4, 5, 15, 1, 43, 20])
print(my_final_result)


#Answer Q2
def find_largestNumber(myLargestNum: list):
    result2 = max(myLargestNum)
    return result2

my_final_result2 = find_largestNumber([2, 3, 4, 5, 15, 1, 43, 20])
print(f"The Largest Number is:", my_final_result2)


#Answer Q3
my_oddList = [n for n in range(1200,2001,125) if n % 2 != 0]
print(f"The Odd Numbers in the List is:", my_oddList)


#Answer Q4
my_slicList = my_oddList [:5]
print(f"The Result of Slicing Numbers in the List is: {my_slicList}")