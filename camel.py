# Write a program that turns a sentence into camel case. The first word is lowercase,
# the rest of the words have their initial letter capitalized,
# and all of the words are joined together
import string

def display():

    msg = 'WELCOME TO CAMELCASE GENERATOR'
    stars = '*' * len(msg)
    print(f'\n {stars} \n {msg} \n {stars}\n')

display()

def main():
    sentence = input("Enter your sentence : ")
    camel = camelCase(sentence)
    print(camel)
    

# Function with data passed in as argument, data output as return value. You can write a test for this. 
def camelCase(sentence):    
    capital = string.capwords(sentence).replace(" ", "")
    camel = capital[0].lower() + capital[1:]
    return camel

main()
