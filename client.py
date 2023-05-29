import time
import socket
import sys

print("Welcome to python chat")
print("")
print("Initializing....")
time.sleep(1)

s = socket.socket()
print("")
host = input(str("Please enter the server adress"))
print("")
name = input(str("Please enter your name:"))
port = 8080
print("")
print("Trying to connect to ",host, "at port ",port)
print("")
time.sleep(1)
s.connect((host,port))
print("Connected")

# connection done

s.send(name.encode())

s_name = s.recv(1024)
s_name = s_name.decode()

print(s_name, " has joined the chat room.")

#message loop

while 1:
    message = s.recv(1024)
    message = message.decode()
    print(s_name, ": ", message)
    message = input(str("Please enter your message:"))
    s.send(message.encode())
    print("Sent")
    
