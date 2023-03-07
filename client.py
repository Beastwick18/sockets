import socket
from time import *
import sys
import time


def main():
    if len(sys.argv) == 3:
        HOST=sys.argv[1]
        PORT=8080
        fileName=sys.argv[2]
    elif len(sys.argv) == 4:
        HOST=sys.argv[1]
        PORT=int(sys.argv[2])
        fileName=sys.argv[3]
    else:
        print('Expected 2 or 3 arguments')
        return
    
    clientSocket = socket.socket()

    print('Client has been established')
    server_add = (HOST, PORT)

    clientSocket.connect(server_add)
    # connect the host and port to the socket
    send_time = time.time()
    clientSocket.send(f'GET /{fileName} HTTP/1.1'.encode('utf-8'))

    header = clientSocket.recv(1024).decode('utf-8')
    data = clientSocket.recv(1024).decode('utf-8')
    recv_time = time.time()
    RTT = recv_time - send_time
    
    headerLines = header.splitlines()
    if headerLines[0] == 'HTTP/1.0 404 Not Found':
        print('Response: 404 Not found')
    elif headerLines[0] == 'HTTP/1.0 200 OK':
        print('Response: 200 OK')
    
    # Sometimes, the header and content messages will be combined,
    # depending on how quickly they were sent. If they were both
    # combined into one message (the header), set the data to be
    # the content after the header.
    if len(headerLines) > 3: # There is data past the header and content type
        data = ''
        for line in headerLines[3:]:
            data += line + '\n'
    
    print(f'Data received by the client is:\n{data}')
    print('RTT ', RTT)

    '''Print other vvalues here '''
    ''' close socket '''
    clientSocket.close()

if __name__ == "__main__":
    main()
