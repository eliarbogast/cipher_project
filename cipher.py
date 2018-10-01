'''
Cipher Project: Takes user input message and password and encrypts it using a "Vignère Cipher"
CS 111, Fall 2018
date: October 2nd, 2018
Names: Eli Arbogast and Drew Garcia
'''

def main():
#Vignere Cipher
	print("* * * VIGNERE CIPHER * * *")

#Prompt user to enter the message to be encoded
	originalMessage = input("Enter the message you want encoded: ")

#Prompt user to enter the password for encoding
	password = input("Enter a password to encrypt this message: ")

#Clean up both user inputs
	originalMessage = originalMessage.lower()
	originalMessage = originalMessage.replace(" ", "")
	password = password.lower()
	password = password.replace(" ", "")

#String to store encrypted characters
	encryptedMessage = " "

#Create a string for the alphabet
	alpha = "abcdefghijklmnopqrstuvwxyz"

#Loop to adjust password length to work with any message
	for i in range(len(originalMessage) - len(password)):
		password = password + password[i]

#Loop to encrypt the message input by the user
	for i in range(len(originalMessage)):
		encryptedChar = (alpha.index(originalMessage[i]) + alpha.index(password[i])) % 26
		encryptedMessage = encryptedMessage + alpha[encryptedChar]

	print(encryptedMessage)




main()
