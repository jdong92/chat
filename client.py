"""
John Dong
May 13, 2013
Programming Assignment #1

client.py
"""

import socket
import os
import select
import sys

#Connection settings

HOST = '127.0.0.1'
PORT = 9050
RECV_BUFFER = 4096

#Function to print out the user handles

def prompt(n):
    sys.stdout.write('<' + n + '>: ')
    sys.stdout.flush()

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error:
    print 'Failed to create socket'
    sys.exit()

s.connect((HOST, PORT))
print 'Connected to remote host. Start sending messages'

#Getting the username

while 1:

    name = raw_input('Please enter a name: ')
    if len(name) > 10:
        print 'Please enter a name less than 10 characters'
    elif name:
        break

prompt(name)

#Using the select function to select between keyboard and socket

while 1:

    socket_list = [sys.stdin, s]

    read_sockets, write_sockets, error_sockets = select.select(socket_list, [], [])

    for sock in read_sockets:
        if sock == s:
            data = sock.recv(RECV_BUFFER)

            if not data:

                print '\nDisconnected from chat server'
                sys.exit()

            else:

                sys.stdout.write(data)
                prompt(name)

        elif sock == sys.stdin:

            msg = sys.stdin.readline()
            s.send('\r<' + name + '>: ' + msg)
            prompt(name)
