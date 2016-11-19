import os
import gnupg

#Step 1: Define strings
path = "/home/pi/Encryption/home1.txt.gpg" #file to be decrypted
output_path = "/home/pi/Desktop/home1.txt" #decrypted file

#step 2: Function to DECRYPT using file path strings as argument
def decrypt (str, str2):
	gpg=gnupg.GPG(gnupghome='/home/pi/.gnupg')
	with open(str, 'r+') as f: status=gpg.decrypt_file(f, passphrase='smtgrd', output=str2)

#Step 3: Call function
decrypt(path, output_path)
