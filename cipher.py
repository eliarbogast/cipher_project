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

#Alphabet string to encrypt
    alphabet = "abcdefghijklmnopqrstuvwxyz"

#Encrypt the input message
    passwordOrd = (ord(i) for i in password)
    originalMessageOrd = ((ord(i) for i in originalMessage))
    passwordLen = len(password)

    for i in range(len(originalMessage)):
        VigCipher = (originalMessageOrd(i) + passwordOrd(i % passwordLen)) % 26
        encryptedMessage = encryptedMessage + alphabet[VigCipher]

    print(encryptedMessage)
 

  
  
 


main()
