import os
#This Program computes command line from python

#TEST 1: with any message file and delete the original message
#os.system('echo encrypting . . . \n')
#os.system('date | tee -a *txt')
#os.system('echo Data stamp added \n')
#os.system('echo smtgrd | gpg --batch --passphrase-fd 0 -c *.txt && rm *.txt')
#os.system('echo encryption is done')


#TEST 2; Adding time stamps
os.system('echo encrypting . . . \n')
os.system('date | tee -a *txt') #time stamps
os.system('echo Date added \n')
os.system('echo smtgrd | gpg --batch --passphrase-fd 0 -c home1.txt && rm home1.txt')
os.system('echo smtgrd | gpg --batch --passphrase-fd 0 -c home2.txt && rm home2.txt')
os.system('echo smtgrd | gpg --batch --passphrase-fd 0 -c home3.txt && rm home3.txt')
os.system('echo encryption is done')

#****Do CA has two text file?
