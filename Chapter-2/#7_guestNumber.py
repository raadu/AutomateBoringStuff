# Takes input of name and number of guests. Then uses conditions to show results.
# Example from page: 53

name=''
while not name:
    print("Enter your name")
    name=input()
print("How many guests will you have?")
numOfGuests=int(input())
if numOfGuests:
    print("Be sure to have enough room for your guests")
print("Done")