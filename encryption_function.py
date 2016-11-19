import os
import gnupg

#Step 1: Define a string

path = "/home/pi/Encryption/home1.txt" #file to be encrypted
output_path= "/home/pi/Desktop/home1.txt.gpg" #encrypted file

#Step 2: Function to encrypt using file path strings as arguments

def encrypt (str, str2):
	gpg=gnupg.GPG(gnupghome='/home/pi/.gnupg')
	with open(str, 'r+') as f: #fetch the file to be encrypted
       		status=gpg.encrypt_file(
       		f, recipients=['4C4E6389'], #public key of recipient (in this case: TA)
       		always_trust='true',
       		output=str2) #output the encrypted file in specified path

#Step 3: Call function
encrypt(path, output_path)

