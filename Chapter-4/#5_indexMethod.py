# Example from 89-92

cats=['pinga','monu','mumin','happy','katto']
cats.append('mika') #adds mika at the end of the list
cats.insert(2,'tao') #insert tao at index 2 and then increase all the following indices
cats.remove('mumin') #remove mumin from the list
cats.sort()
# To sort alphabetically reverse (Z to A) type: cats.sort(reverse=True)
# List containing both number and strings cannot be sorted with sort()

print(cats)