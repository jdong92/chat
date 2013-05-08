import socket

HOST = '127.0.0.1'
PORT = 12345

try:
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error:
    print 'Failed to create socket'
    sys.exit()

client.connect((HOST, PORT))

client.send('Hi')
client.recv(1024)
client.close()
