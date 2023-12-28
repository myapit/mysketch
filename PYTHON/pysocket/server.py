# python socket server example

import socket

HOST = socket.gethostbyname(socket.gethostname()) ## dynamic IP address
#HOST = "127.0.0.1"
PORT = 9090

myserver = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
myserver.bind((HOST, PORT))

myserver.listen(10) ## accept 10 connection only

print(f"Server starting ... {HOST} ")

while True:
    comm_socket, ipaddress = myserver.accept() # accept() will return 2 value, comm_socket and address
    print(f"Connected to {ipaddress}")
    mesg = comm_socket.recv(1024).decode('utf-8') # receive 1024 bytes
    print(f"Message from client : {mesg}")
    comm_socket.send(f"Got your message ! TQ".encode('utf-8'))
    comm_socket.close()
    print(f"Connection with {ipaddress} ended")
