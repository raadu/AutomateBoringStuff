# This program returns a string based on random arguments passed in the function
# Example from page: 65
# This is just a slightly changed program of the previous one

import random

def getAnswer(answerNumber):
    if answerNumber==1:
        return "It is certain"
    elif answerNumber==2:
        return "It is decidedly so"
    elif answerNumber==3:
        return "Yes"
    elif answerNumber==4:
        return "Reply hazy try again"
    elif answerNumber==5:
        return "Ask again later"
    elif answerNumber==6:
        return "Concentrate and ask again"
    elif answerNumber==7:
        return "My reply is no"
    elif answerNumber==8:
        return "Outlook not so good"
    elif answerNumber==9:
        return "Very doubtful"

print(getAnswer(random.randint(1,9))) #instead of writing three lines of the previous code example on page:64