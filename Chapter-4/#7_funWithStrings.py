# String is also a list. There are multiple characters making up a string. So methods of list can be applied in strings too.
# Example of page 94 of the book.

name='Motabbir Hossain'


print(name[0])
print(name[3])
print(name[8])
print(name[-3])
print('Ho' in name)
print('Mu' in name)
print('ik' not in name)
print('ssa' not in name)

for i in name:
    print('# # # * * ='+i+'= * * # # #')
