# Example from page 70


def spam():
    global eggs
    eggs='spam'


eggs='global'
spam()
print(eggs)