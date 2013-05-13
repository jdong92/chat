"""
John Dong
May 13, 2013
Programming Assignment #1

server.py
"""

import socket
import os
import select
import sys

#Connection settings

PORT = 9050
HOST = '127.0.0.1'
RECV_BUFFER = 4096

#Function to print out the user handles

def prompt(n):
    sys.stdout.write('<' + n + '>: ')
    sys.stdout.flush()

try:
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except:
    print 'Failed to create socket'
    sys.exit()

server_socket.bind((HOST, PORT))
server_socket.listen(10)

input = [server_socket, sys.stdin]

print 'Chat Program'

while 1:

    name =  raw_input('Please enter a name: ')
    if len(name) > 10:
        print 'Please enter a name less than 10 characters'
    elif name:
        break

prompt(name)

#Using the select function which allows to select different inputs

while 1:

    inputready, outputready, exceptready = select.select(input,[],[])

    for sock in inputready:

        if sock == server_socket:

            client, address = server_socket.accept()
            input.append(client)

        elif sock == sys.stdin:

            data = sock.readline()
            prompt(name)

            for s in input:
                if s not in (server_socket, sys.stdin):
                    s.send('\r<' + name + '>: ' + data)
        else:

            data = sock.recv(RECV_BUFFER)
            if data:
                sys.stdout.write(data)
                prompt(name)

server_socket.close()

