# String data type is immutable. So it does not support adding a new string or character.
# But can be done by slicing the string and then concatenating a new string. Example from page 94-94 of the book.


food='Burger'
foodShop=food[0:6]+' King'

print(food)
print(foodShop)