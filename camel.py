# Write a program that turns a sentence into camel case. The first word is lowercase,
# the rest of the words have their initial letter capitalized,
# and all of the words are joined together
import string

def display():

    msg = 'WELCOME TO CAMELCASE GENERATOR'
    stars = '*' * len(msg)
    print(f'\n {stars} \n {msg} \n {stars}\n')

display()

def camelCase():
    sentence = input("Enter your sentence : ")
    capital = string.capwords(sentence).replace(" ", "")
    camel = capital[0].lower() + capital[1:]
    print(camel)

camelCase()