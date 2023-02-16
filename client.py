
import socket
from time import *
import sys
import time

HOST='127.0.0.1'
PORT=25565
fileName='test.txt'



clientSocket = socket.socket()

print('Client has been established')
server_add = (HOST, PORT)

clientSocket.connect(server_add)
# connect the host and port to the socket
send_time = time.time()
clientSocket.send(b'0101')


data=clientSocket.recv(1024)
recv_time = time.time()
RTT = recv_time - send_time
print('Data received by the client is', data)
print('RTT ', RTT)

'''Print other vvalues here '''
''' close socket '''
clientSocket.close()
