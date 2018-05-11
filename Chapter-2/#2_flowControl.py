# A program that takes input of Name and Age. Then check some conditions.
# This program is from page: 41

print("Enter Name: ")
name=input()
print("Enter Age: ")
age=int(input())

if name == "Alice":
    print("Hi, Alice")
elif age < 12:
    print("You are not Alice, Kiddo")
elif age > 2000:
    print("Unlike you, ALice is not an undead, immortal vampire")
elif age > 100:
    print("You are not Alice, grannie")
