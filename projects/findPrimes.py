#!/usr/bin/env python3
#Author: G//05t
#findPrimes.py

print('\nProgram to find the prime factors (p and q) to solve n')
productN = int(input('Enter the product n: '))

i = 1

while(i <= productN):
    count = 0
    if(productN % i == 0):
        x = 1
        while(x <= i):
            if(i % x == 0):
                count += 1
            x += 1
        if(count == 2):
            print(f'\n{i} is a Prime Factor of the Number {productN}')
    i += 1

