import os
import time
import datetime
import gnupg
import random

myfloat = 10.0
myfloat = float(10)
random.seed()
#Step 1: Define strings with original and encrypted file locations

path = "/home/pi/Documents/info4.xml" #file to be encrypted
output_path= "/home/pi/Documents/info4.xml.gpg" #encrypted file

#-------------------------------------------------------------------------------------------

#Step 2: Encryption function

while True:
	with open("/home/pi/Documents/info4.xml", "a") as f:
		f.write("" + datetime.datetime.now().strftime("%H:%M:%S") + " this line contains the data" + "\n")

	def encrypt (str, str2):
		gpg=gnupg.GPG(gnupghome='/home/pi/.gnupg')
		with open(str, 'r+') as f: #fetch the file to be encrypted
			status=gpg.encrypt_file(
			f, recipients=['2435A1BD'], #public key of recipient (in this case: Transformer)
			always_trust='true',
			output=str2) #output the encrypted file in specified path

#-------------------------------------------------------------------------------------------
			
#Step 3: Calling the encryption function and sending the encrypted file
			
	encrypt(path, output_path) #calling the encryption function

	os.system('rm info4.xml') #removing the xml from the home database to save memory

	os.system('scp /home/pi/Documents/info4.xml.gpg root@192.250.70.251:/home/guest/smartgrid/') #sending the encrypted XML file to the transformer

	time.sleep(myfloat*(random.random())) #delay the sending of the next generated XML file by a random time


