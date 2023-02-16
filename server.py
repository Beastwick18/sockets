
# Import socket module
import socket

# Import thread module


# Create a TCP server socket


serverSocket = socket.socket()  

# Assign a port number
serverPort = 25565


# Bind the socket to server address and server port

serverSocket.bind(('127.0.0.1', serverPort))

# Listen to at most 5 connection at a time

serverSocket.listen()

# Server should be up and running and listening to the incoming connections

def multi_thread(connectionSocket):
    try:

        # Extract the path of the requested object from the message


        message = connectionSocket.recv(1024).decode('utf-8')

        f = open(message,'rb')

        # Store the entire contenet of the requested file in a temporary buffer

        outputdata = f.read()
        print(outputdata)


        # Send the HTTP response header line to the connection socket


        # Send the content of the requested file to the connection socket
    except:
        pass


    # Close the socket in case of some issues 
    connectionSocket.close()


while True:
    '''This part is for multi threading'''
    print('Ready to serve')
    '''Start the new thread'''







