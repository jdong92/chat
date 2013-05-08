import socket
import os
import select
import sys

HOST = '127.0.0.1'
PORT = 9050

print 'Chat Program'

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error:
    print 'Failed to create socket'
    sys.exit()

s.connect((HOST, PORT))

while 1:

    socket_list = [sys.stdin, s]

    read_sockets, write_sockets, error_sockets = select.select(socket_list, [], [])

    for sock in read_sockets:
        if sock == s:
            data = sock.recv(4096)
            """
            if not data:
                print '\nDisconnected from chat server'
                sys.exit()
            else:
                #print data
                sys.stdout.write(data)
                sys.stdout.write('<You> ')
                sys.stdout.flush()
            """
            if data:
                print data

        else:
            msg = sys.stdin.readline()
            s.send('<Client>: ' + msg)
            sys.stdout.write('<You> ')
            sys.stdout.flush()
