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

 # Create the code alphabet
	# Remove duplicate letters from the password
	# Idea: Look at each letter in turn. If we haven't seen it, copy it over to the new password storage string.
	passwordNoDupes = ""
	for ch in password:
		if ch not in passwordNoDupes:
			passwordNoDupes = passwordNoDupes + ch


#String to store encrypted characters
	encryptedMessage = " "

	for i in range(len(originalMessage)):
		ch_origin = originalMessage[i]
		ch_pass = password[i]

		#Formula used below to simplify process without needing to create alphabet strings
		encrypted_ord = (ord(ch_origin)+ord(ch_pass))%26
		encryptedMessage = encryptedMessage + chr(encrypted_ord)
		print(encryptedMessage)

    print(encryptedMessage)

	#Wait for user input to close the window
	raw_input()




main()
