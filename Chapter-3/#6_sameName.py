# Example program from page 69

def spam():
    eggs='spam local'
    print(eggs)

def bacon():
    eggs='bacon local'
    print(eggs)
    spam()
    print(eggs)

eggs='global'
bacon()
print(eggs)