# Example problem of page 70-71

def spam():
    global eggs
    eggs='spam'

def bacon():
    eggs='bacon'

def ham():
    print(eggs)

eggs=42
spam()
print(eggs)