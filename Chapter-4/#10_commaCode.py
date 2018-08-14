# Practice project in page 102 of the book

spam=['apples','bananas','tofu','cats']

def commaCode(spam):
    line=str(spam[-1])  # Put the last element of the list in a variable named line
    spam2='and '+line   # Add 'and' string before that selected last element of the list
    spam[-1]=spam2      # Replace the last element of the list with edited string spam2
    string=', '.join(spam)  # use comma, spacing and jon function to put all the elements in a variable named string
    print(string)   # print the string variable containing all the list elements stored as strings

# This works even if the main spam list is changed (added more elements or reduced


commaCode(spam)