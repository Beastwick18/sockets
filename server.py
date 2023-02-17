import re
import sys
import mimetypes

# Import socket module
import socket

# Import thread module
from threading import Thread, Event

def not_found_response(connectionSocket, error):
    print('404 Not Found')
    connectionSocket.send('HTTP/1.0 404 Not Found\r\nContent-Type: text/html\r\n\r\n'.encode('utf-8'))
    connectionSocket.send(f'<html><body><h1>Error 404: Not Found</h1><p>{error}</p></body></html>'.encode("utf-8"))

def ok_response(connectionSocket, filename):
    content = mimetypes.guess_type(filename)[0]
    print(f'Content type: {content}')
    connectionSocket.send(f'HTTP/1.0 200 OK\r\nContent-Type: {content}\r\n\r\n'.encode('utf-8'))

def parse_request(message):
    lines = message.splitlines()
    for line in lines:
        words = line.split()
        # Check that the line matches GET (filename) ...
        if len(words) == 3 and words[0] == 'GET':
            if match := re.match('/(.*)', words[1]):
                filename = match.group(1)
                if not filename: # if no file provided (e.g. 127.0.0.1/) provide default of index.html
                    return None
                
                return filename
    return None

def multi_thread(connectionSocket):
    try:
        # Extract the path of the requested object from the message
        message = connectionSocket.recv(1024).decode('utf-8')
        print(message)
        filename = parse_request(message)

        if filename is not None:
            # Store the entire content of the requested file in a temporary buffer
            f = open(filename, 'rb')
            outputdata = f.read()

            # Send the HTTP response header line to the connection socket
            print('Sending header...')
            ok_response(connectionSocket, f.name)
            
            # Send the content of the requested file to the connection socket
            print('Sending file...')
            connectionSocket.send(outputdata)
        else:
            not_found_response(connectionSocket, 'Could not find GET request')
    except Exception as e:
        error = f'{type(e).__name__}: {str(e)}'
        not_found_response(connectionSocket, error)

    # Close the socket in case of some issues 
    connectionSocket.close()

def main():
    # Create a TCP server socket
    serverSocket = socket.socket()

    # Assign a port number
    if len(sys.argv) <= 1:
        serverPort = 8080
    else:
        serverPort = int(sys.argv[1])

    # Bind the socket to server address and server port
    serverSocket.bind(('', serverPort)) # default to localhost

    # Listen to at most 5 connection at a time
    serverSocket.listen(5)

    # Server should be up and running and listening to the incoming connections

    print('Ready to serve')
    while True:
        '''This part is for multi threading'''
        conn, addr = serverSocket.accept()
        print(f'Connected to: {str(addr)}')
        thread = Thread(target=multi_thread, args=(conn,))
        '''Start the new thread'''
        thread.start()
    
    # Close server socket
    serverSocket.close()

if __name__ == '__main__':
    main()
