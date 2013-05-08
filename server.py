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

host = '127.0.0.1'
port = 12345

listenfd.bind((host, port))
listenfd.listen(10)
input = [listenfd, sys.stdin]

running = 1

while running:

    inputready, outputready, exceptready = select.select(input,[],[])

    for s in inputready:

        if s == listenfd:
            client, address = listenfd.accept()
            input.append(client)
        elif s == sys.stdin:
            junk = sys.stdin.readline()
            running = 0
        else:
            data = s.recv(1024)
            if data:
                print data
            else:
                s.close()

listenfd.close()

