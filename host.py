import time
import socket
import sys

print("Welcome to python chat")
print("")
print("Initializing....")
time.sleep(1)

s = socket.socket()
host = socket.gethostname()
port = 8080
s.bind((host,port))
print("")
print(host)

name = input(str("Please enter your username:"))

s.listen(1)
print("")
print("Waiting for any incoming connections...")
print("")
conn, addr = s.accept()
print("Received Connections")

#connection done
s_name = conn.recv(1024)
s_name = s_name.decode()
print(s_name, "has connected to the chat room")
print("")
conn.send(name.encode())

#message loop
while 1:
    message = input(str("Please enter your message:"))
    conn.send(message.encode())
    print("Sent")
    message = conn.recv(1024)
    message = message.decode()
    print(s_name, ": ", message)
    

