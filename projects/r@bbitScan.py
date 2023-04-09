#!/usr/bin/env python3
#r@bbit_scan.py

import socket
import time

startTime = time.time()
portList = []

def demPorts():
    print('\nEnter each port you would like to scan one-by-one')
    print('If you are satisfied with port selection enter the number: 0')
    print('------------------------------------------------------------')
    while True:
        port = int(input('Port: '))
        portList.append(port)
        if (port == 0):
            break
    return portList.sort()

print('\n~~~~~~~~~~~~~R@bbit\'s Port Scanner~~~~~~~~~~~~~')
print('##################################################')
target = input('Enter the IP of the host you like to scan: ')
#target_IP = socket.gethostbyname(target)       #Could add to scan by hostname
print('##################################################')

demPorts()
print(f'\nScanning Ports: {portList}')

answer = input('\nIs this correct?[y/n] ')

if answer.lower() in ['y', 'yes']:
    pass
elif answer.lower() in ['n', 'no']:
    portList.clear()
    demPorts()
else:
    print('\nTry Again >.<')
    exit(1)

print(f'\nInitiating Scan for host: {target}        /)/)')
print(f'=====================================      (?.?)')
print(f'Ports Targeted: {portList}')

for x in portList:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as scanner:
        conn = scanner.connect_ex((target,x))
        if (conn == 0):
            print(f'Port {x}: OPEN')

endTime = time.time()
totalTime = endTime - startTime
print(f'\nTotal time of scan: {totalTime}')
print('\nWOOT! (\ /)')
print('      (O.o)')
