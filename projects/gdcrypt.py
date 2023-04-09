#!/usr/bin/env python3
#Author: G//05t
#gdcrypt.py

import sys, getopt
from itertools import cycle

def main(argv):
    usage = 'Usage: python gdcrypt.py -i <EncryptedFile>' 
    options = 'hi:'

    if len(argv) < 1 or len(argv) > 2:
        print(usage)
        sys.exit()
    try:
        opts, args = getopt.getopt(argv,options)
        for opt, arg in opts:
            if opt == '-h':
                print(usage)
                sys.exit()
            elif opt == '-i':
                decrypt(argv[1])
            else:
                print(usage)
                sys.exit()
    except getopt.GetoptError:
        print(usage)
        sys.exit(2)

def decrypt(eFile):
    print('\n\t\t***G//05t\'s XOR Machine ***')
    print('\t\t==========ToDecrypt===========')

    key = input('\nEnter Encryption Key: ')

    with open(eFile, 'rb') as f:
        cryptedMessage = f.read().decode()
        plainText = ''.join(chr(ord(x)^ord(y)) for x,y in zip(cryptedMessage, cycle(key)))

    print(f'\nMessage: {plainText}')

if __name__ == "__main__":
    main(sys.argv[1:])
