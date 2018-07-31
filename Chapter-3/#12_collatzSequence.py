# Practice problem Collatz Sequence of page 77

def collatz(number): # a collatz function to calculate
    if number%2==0: # if number is even
        print(number//2)
        return number//2 # then do this
    elif number%2==1:  # if number is odd
        print(3*number+1)
        return 3*number+1 # then do this


print("Input Number:\n")

while True:
    try:
        number=int(input()) # take integer input from user
        if number<=0:  # checke for negative integers
            print("Sorry, wrong input. Insert positive integer number:\n")
            continue  # continue the loop
        break  # if positive ineteger value added then break

    except ValueError: # if wrong value like string added
        print("Sorry, wrong input. Insert integer number:\n")
        continue # continue the loop

while number!=1:
    number=collatz(number) # do recursion until the result is 1