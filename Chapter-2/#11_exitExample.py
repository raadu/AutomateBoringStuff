# This program exits only when "exit" is typed in input
# Example from page: 58

import sys

while True:
    print("Enter input: ")
    response=input()
    if  response=="exit":
        sys.exit()
    print("You typed "+response)
