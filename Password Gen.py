#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))
nr_Specific= input('is there anyhting you want to add specifically. yes or no: ')

if nr_Specific=='yes':
    nr_Specific=input('what?')
else:
    nr_Specific=''

password=""
passList=[]
for i in range(0,nr_letters):
    randChar=random.choice(letters)
    passList.append(randChar)

for i in range(0,nr_numbers):
    randNum=random.choice(numbers)
    passList.append(randNum)

for i in range(0,nr_symbols):
    randSymbols=random.choice(symbols)
    passList.append(randSymbols)

if nr_Specific!='':
    passList.append(nr_Specific)

random.shuffle(passList)

for i in passList:
    password += i
print('--------------')

print('Here is your Password: '+password)   