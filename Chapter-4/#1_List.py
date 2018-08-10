# some basic functions of lists. From page 80-84 from the book.

list=['sa','re','ga','ma','pa','dha']
list2=[1,2,3,4,5,6]
list3= [['sa','re','ga','ma','pa','dha'],[1,2,3,4,5,6]]

# get a value from list index 2
print(list[2])

# print string with the index value
print('This is index 3: '+list[3])

# get value from a list containing lists
print(list3[0][4])
print(list3[1][3])

# negative index values
print(list2[-1])
print(list[-2])

# getting sublists with slicing
print(list[1:4])
print(list[:4])

# get length of list
print(len(list2))
print(len(list3))

# change a value in the list
list[2]='change'
print(list)

# concatenate two lists
list4=list+list3
print(list4)

# removing value from a list
del list2[3]
print(list2)

