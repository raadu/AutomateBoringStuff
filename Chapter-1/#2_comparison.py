# This program take two numbers in A and B variable. Then compares and shows the boolean results of these two variables.
#This program is to show example in page: 33 and 34.

print("Enter A: ")
A=input()
print("Enter B: ")
B=input()

equalTo=(A==B)
print("A equal to B is: " +str(equalTo))

notEqualTo=(A!=B)
print("A not equal to B is: " +str(notEqualTo))

lessThan=(A<B)
print("A less than B is: " +str(lessThan))

greaterThan=(A>B)
print("A greater than B is: " +str(greaterThan))

lessThanOrEqual=(A<=B)
print("A less than or equal to B is: " +str(lessThanOrEqual))

greaterThanOrEqual=(A>=B)
print("A greater than or equal to B is: " +str(greaterThanOrEqual))