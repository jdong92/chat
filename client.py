import socket
import os
import select
import sys

HOST = '127.0.0.1'
PORT = 9050

print 'Chat Program'

try:
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error:
    print 'Failed to create socket'
    sys.exit()

client.connect((HOST, PORT))
"""
client.send("Hi")
while 1:
    data = client.recv(4096)
    if data:
        print data
"""

while 1:
    sys.stdout.write('<You>: ')
    msg = sys.stdin.readline()
    client.send(msg)
    sys.stdout.flush()
