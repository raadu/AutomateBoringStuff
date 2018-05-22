# Prompts a name and password. Uses conditions to see if the name matches to "Joe" and password matches to "swordfish".
# Example from page: 51

while True:
    print("What is your name?")
    name=input()
    if name!="Joe":
        continue
    print("Hello Joe, What is the password? (It is a fish)")
    password=input()
    if password=="swordfish":
        break
print("Access Granted") #check out for indentation!