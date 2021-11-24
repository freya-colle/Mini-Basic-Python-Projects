"""
Project 3 - PRINT EVEN/ODD LENGTH WORDS IN A STRING
Given a string. The task is to print all words with even length in the given string.
"""

#PRINT EVEN LENGTH WORD

def print_even_word(string2):
    string2 = string2.split(' ')

    for word in string2:
        if len(word)%2 == 0:
            print(word)

string2 = input('Even_string2 ',)
print_even_word(string2)

#PRINT ODD LENGTH WORD
def print_odd_word(s3):
    s3 = s3.split()
    for word in s3:
        if len(word)%2 != 0:
            print(word)
s3 = input('Odd_string3 = ',)
print_odd_word(s3)

#COMBINE THE TWO SYNTAX
def print_even_odd_word(s9):
    s9 = s9.split()
    for word in s9:
        if len(word)%2 == 0:
            print('Even length word: ', word)
        else:
            print('Odd length word: ', word)
s9 = input('s9 = ', )
print_even_odd_word(s9)
