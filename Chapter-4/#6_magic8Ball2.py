# Example from page 92 of the book
# An uodated version of previous magic8Ball program. Here List is used instead of lots of if-elses

import random

messages=['It is certain','It is decidedly so','Yes, defiitely','Reply hazy try again',\
          'Ask again later','Concentrate and ask again','My reply is no','Outlook not so good',
          'Very doubtful']

# You can use indentation to make the list look readable. Can use Backslash (\) to indicate there is a line below.
# Or dont use \. No prob.
print(messages[random.randint(0,len(messages)-1)])