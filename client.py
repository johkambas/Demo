from datetime import datetime
from socket import *
from time import time

def main():
    serverName: 'Localhost'
    serverPort: 12000
    clientSocket: socket(AF_INET, SOCK_DGRAM)
    message: 'Ping'
    counter = 10
    i: 0
    remain: counter - i
    print(counter, 'pings are being tried. \n')
    while i < counter:
        i += 1
    print('\nPing attempt number', i, 'is currently in progress.\n')
    print(remain, 'attempts remain. \n')
    dt = datetime. now()
    clientSocket.sendto(message(serverName, serverPort))
    clientSocket.settimeout(1)
    try:
        modifiedMessage, serverAddress= clientSocket.recvfrom(1024)
        dt2 = datetime.now()
        et = dt - dt2
        print(modifiedMessage)
        print('Time elapsed:', et.microseconds, 'microseconds\n')
    except timeout:
        print("Request timed out.")
    if i == 10:
        clientSocket.close()
pass
if __name__ == '__main__':
    main()