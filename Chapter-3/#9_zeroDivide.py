# Exception handling example given in page 73

def div(divideby):
    try:
        return 42/divideby
    except ZeroDivisionError:
        print("Sorry, Invalid Input Found")


print(div(100))
print(div(6))
print(div(1.2))
print(div(1))
print(div(0))
