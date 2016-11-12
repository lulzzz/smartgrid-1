import os
import gnupg

#Step 1: add time stamps 

os.system('date | tee -a *txt')


#Step 2: encrypt the file with public key provided

gpg=gnupg.GPG(gnupghome='/home/pi/.gnupg')

with open('home1.txt', 'rb') as f:
	status=gpg.encrypt_file(
	f, recipients=['4C4E6389'], #enter encryption key of TA here which was imported
	always_trust='true',
	output='home1.txt.gpg')

with open('home2.txt', 'rb') as f:
        status=gpg.encrypt_file(
        f, recipients=['4C4E6389'],
        always_trust='true',
        output='home2.txt.gpg')

with open('home3.txt', 'rb') as f:
        status=gpg.encrypt_file(
        f, recipients=['4C4E6389'],
        always_trust='true',
        output='home3.txt.gpg')

#Step 3: Remove .txt files to save memory

os.system('rm home1.txt && rm home2.txt && rm home3.txt')

