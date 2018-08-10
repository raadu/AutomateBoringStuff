# using in and not in in a program. Example from page 87 of the book.

catNames=['Happy','Milo','Pinga','Kalu']

print("Enter a cat name: ")
name=input()
if name in catNames: # use 'not in' to show cat names not inside the list
    print("I have a cat named "+name)
else:
    print("I do not have a cat named "+name)

