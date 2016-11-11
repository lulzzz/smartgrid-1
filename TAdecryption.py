
#receiver decryption
import os

# Step 1: Decrypting
os.system('echo Decryption . . . \n ')

os.system('echo smtgrd | gpg --batch -o home1.txt --passphrase-fd 0 --decrypt home1.txt.gpg && rm home1.txt.gpg')
os.system('echo smtgrd | gpg --batch -o home2.txt --passphrase-fd 0 --decrypt home2.txt.gpg && rm home2.txt.gpg')
os.system('echo smtgrd | gpg --batch -o home3.txt --passphrase-fd 0 --decrypt home3.txt.gpg && rm home3.txt.gpg')

os.system('echo Decryption Successful!!\n')


# Step 2: Option 1: Logging all data       
# Appending new file into original file located in TA.
# title for file is distinguished by customer ID 16 digits.
#os.system('1234567891234567n.txt >> 1234567891234567.txt')
#os.system('echo smtgrd | gpg --batch -o test2.txt --passphrase-fd 0 --decrypt test2.txt.gpg && rm test2.txt.gpg')
 
#Step 2: Option 2: Logging all data         
#Appending new file into original file located in TA
#title for file is distinguished by Home ID
os.system('cat home1.txt >> logHome1.txt')
os.system('cat home2.txt >> logHome2.txt')
os.system('cat home3.txt >> logHome3.txt')


