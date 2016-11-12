#decryption at the TA

import os
import gnupg

#Step 1: Decryption + removing .gpg file to save memory
os.system('echo Decrypting... \n')


#os.system('echo smtgrd | gpg --batch -o home1.txt --passphrase-fd 0 --decrypt home1.txt.gpg && rm home1.txt.gpg')
#os.system('echo smtgrd | gpg --batch -o home2.txt --passphrase-fd 0 --decrypt home2.txt.gpg && rm home2.txt.gpg')
#os.system('echo smtgrd | gpg --batch -o home3.txt --passphrase-fd 0 --decrypt home3.txt.gpg && rm home3.txt.gpg')

gpg=gnupg.GPG(gnupghome='/home/pi/.gnupg')
with open('home1.txt.gpg', 'rb') as f:
	status=gpg.decrypt_file(f, passphrase='smtgrd', output='home1.txt')

gpg=gnupg.GPG(gnupghome='/home/pi/.gnupg')
with open('home2.txt.gpg', 'rb') as f:
        status=gpg.decrypt_file(f, passphrase='smtgrd', output='home2.txt')

gpg=gnupg.GPG(gnupghome='/home/pi/.gnupg')
with open('home3.txt.gpg', 'rb') as f:
        status=gpg.decrypt_file(f, passphrase='smtgrd', output='home3.txt')


os.system('echo Decryption Successfull. \n')

#Step 2: Logging all data in a log file (appending log file when additional data comes)

os.system('cat home1.txt >> logHome1.txt')
os.system('cat home2.txt >> logHome2.txt')
os.system('cat home3.txt >> logHome3.txt')

os.system('Log files updated succesfully')

