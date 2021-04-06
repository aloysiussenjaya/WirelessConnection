import socket

HOST = '192.168.100.49'
PORT = 7500

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #todo: you can replace here if you want to change IP Family and Protocol 
s.bind((HOST, PORT)) #! just put HOST, PORT in the parameter
s.listen(5) #todo: you can replace the parameter with anything with integer type to change the waiting time 

while True:
    clientsocket, address = s.accept()
    print(f"Connection from {address} has enstablished!")
    clientsocket.send(bytes("Welcome to the server!","utf-8")) #* sending bytes data that encoded with utf-8
    clientsocket.close()