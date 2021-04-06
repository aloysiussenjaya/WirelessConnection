import socket

HOST = '192.168.100.14'
PORT = 6000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #TODO: you can replace here if you want to change IP Family and Protocol 
s.connect((HOST, PORT)) #! just put HOST, PORT in the parameter

#msg = s.recv(8) #receive bytes data with buffer 8 #TODO: you can use this if you only want get specific character limit not all data by change the buffer
#print(msg.decode("utf-8"))

full_msg = ''
message = ''
while True:
    msg = s.recv(8)
    if len(msg) <= 0:
        break
    full_msg += msg.decode("utf-8")

print(full_msg) #! decode and encode use utf-8