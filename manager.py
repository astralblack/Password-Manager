# Title: Nitrogen
# Description: Easy password managment for when ever you need your password.
# Author: Created by Astral

# Variables
data = open('data.txt')
menu = ['1','2']

# Functions
def writeValue():
        clear_screen()
        user_input = input("Type the password you would like for us to store")
        with open('data.txt','w')as data:
                print(user_input, ' has been stored')
                data.write(user_input)
                data.close()

def loadValue():
        clear_screen()
        with open('data.txt', 'r') as data:
                print ('Your password is ' + data.read())
                data.close()

def clear_screen():
        print("\n" * 100)

# Bulk of code
print('Press 1 for storing passwords\n')
print('Press 2 for reading existing passwords')
menu_input = input('What would you like to do? ')
print(menu_input)

if menu_input == "1":
        writeValue()

elif menu_input == "2":
        loadValue()


