import socket
s = socket.socket()
host = socket.gethostname()
port=8080
s.bind((host,port))
s.listen(1)
print("Waiting for 2 connections...")
conn,addr = s.accept()
print("Client 1 has connected...")
conn.send("Welcome to the server".encode())
conn1, addr1 = s.accept()
print("Client 2 has connected...")
conn1.send("Welcome to the server".encode())
