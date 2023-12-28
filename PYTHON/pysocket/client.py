import socket
import sys


# checking argv when not hardcode IP server

if len(sys.argv) < 2:
    print(f"Command : {sys.argv[1]} IP-Address")
else:
    print("executing ...")

#HOST = '172.17.0.2' # IP of server
HOST = sys.argv[1]
PORT = 9090



myclient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
myclient.connect((HOST, PORT))

myclient.send("Hai there".encode('utf-8'))
print(myclient.recv(1024).decode('utf-8'))