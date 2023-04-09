#!/usr/bin/env python3
#Author: G//05t
#gcrypt.py

from itertools import cycle

print('\n\t\t***G//05t\'s XOR Machine ***')
print('\t\t==========ToEncrypt===========')

print('\nThis program creates an encrypted file in the current directory\nthat can be decrypted by gdcrypt.py with key.')

eFile = input('\nEnter FileName: ')
key = input('Enter Encryption Key: ')
message = input('Enter Message for Encryption: ')

cryptedMessage = ''.join(chr(ord(x)^ord(y)) for x,y in zip(message, cycle(key)))

print(f'\nCrypted Message: {cryptedMessage}')
print(f'\nEncoded Crypted Message: {cryptedMessage.encode()}')

with open(eFile, 'wb') as f:
    f.write(cryptedMessage.encode())

print('\nComplete!')
print('Share File and Key with friend for fun')
