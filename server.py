import socket
import os
import select
import sys

try:
    listenfd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error:
    print 'Failed to create socket'
    sys.exit()

print 'Chat Program'
#userName = raw_input('Please enter a username: ')

HOST = '127.0.0.1'
PORT = 9050
maxline = 4096

listenfd.bind((HOST, PORT))
listenfd.listen(10)
input = [listenfd, sys.stdin]

running = 1

while running:

    inputready, outputready, exceptready = select.select(input,[],[])
    for s in inputready:
        if s == listenfd:
            client, address = listenfd.accept()
            input.append(client)
        else:
            data = s.recv(maxline)
            if data:
                print data
                #s.send(data) #Can't send back because it receive it yet
            else:
                s.close()
                input.remove(s)
            """
            msg = sys.stdin.readline()
            listenfd.send('Report')
            sys.stdout.write(userName + '> ')
            sys.stdout.flush()
            """

listenfd.close()

