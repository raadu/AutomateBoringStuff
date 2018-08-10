# using list to store cat names. From page 85 of the book.

catNames=[]

while True:
    print("Enter name of the cat "+str(len(catNames)+1)+" or enter nothing to stop adding")
    name=input()
    if name=="":
        break
    catNames=catNames+[name]
print("The cat names are:")
for name in catNames:
    print(' '+name)