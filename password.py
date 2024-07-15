#imports string module
import string

#imports random module
import random

#prompts user for password length
length = int(input("Enter password length: "))

#To check input length is greater than 8 
if length<8:
	print("Password should be at least 8")
	print("\n")
	length = int(input("Enter password length again:"))

else:
	pass
	
#using triple quotes(''') for multi line strings	
print('''Choose character set for password from these : 
		1. Digits
		2. Letters
		3. Special characters
		4. Exit''')

charList = ""

# Selecting character set for password
while(True):
	
	#prompts user to choose a number
	user_choice = int(input("Choose a number "))
	
	if(user_choice == 1):
		# Adds letters to  characters
		charList += string.ascii_letters

	elif(user_choice == 2):
		# Adds digits to characters
		charList += string.digits

	elif(user_choice == 3):
		# Adds special characters to characterlist
		charList += string.punctuation

	elif(user_choice == 4):
		break
	
	else:
		print("Please select a valid option!")

password = []

for i in range(length):

	# Selecting random character from our character list
	randomchar = random.choice(charList)
	
	# appending a random character to password
	password.append(randomchar)

#prints password as a string
print("The random password is " + "".join(password))

