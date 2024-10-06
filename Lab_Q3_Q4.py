#Q3: Create an odd numbers list from the elements of a range from 1200 to 2000 with steps of 125, using [ List Comprehension ].
odd_numlist = [x for x in range(1200, 2000, 125) if x % 2 != 0]
print("The odd numbers are:", odd_numlist)

#Q4: use list slicing to get a new list from the previous list (odd numbers list) starting from the start to the 5th element in the list.
new_list=odd_numlist[:5]
print("Items in List start from 5th to last index are: ",new_list)