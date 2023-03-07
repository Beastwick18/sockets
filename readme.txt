In order to run this code, you must have python 3

To start the server, run the following command:
    python3 server.py <port>
where <port> is the port number you want the server to run on. This parameter is optional, and will default to 8080.
the ip address is always localhost or 127.0.0.1, or whatever your machines ip address is

To start the client, run the following command:
    python3 client.py <server_ip_address> <port> <requested_file_name>
or...
    python3 client.py <server_ip_address> <requested_file_name>
<server_ip_address> is the ip address of a running instance of the server.py code
<port> is the port of a running instance of the server.py code, not the client's port
    <port> is also optional, and will default to 8080
<requested_file_name> is the file you wish to recieve from the server.
    The file location must be relative to the current working directory of the running server.py instance
    No preceding '/' should be present before the filename.
    Files nested in directories are fine, however.

To connect in a browser, type in the following address into the address bar:
    http://<server_ip_address>:<port>/<requested_file_name>
Here, <server_ip_address>, <port>, and <requested_file_name> refer to the same parameters as listed above for client.py.
