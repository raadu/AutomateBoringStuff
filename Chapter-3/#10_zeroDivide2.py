# Exception handling example given in page 73. Here try-except used in print functions.

def div(divideby):
    return 42/divideby


try:
    print(div(100))
    print(div(6))
    print(div(1.2))
    print(div(1))
    print(div(0))
except ZeroDivisionError:
    print("Error")
