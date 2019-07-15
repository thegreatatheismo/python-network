#!/usr/bin/python

import socket
import threading

bind_ip = raw_input("Enter and IP Address: ")
bind_port = int(raw_input("Enter a port: "))

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((bind_ip,bind_port))

server.listen(5)

print "[*] Listening on %s:%d" % (bind_ip,bind_port)

def handle_client(client_socket):

    request = client_socket.recv(1024)
    
    print "[*] Recieved: %s" % request

    client_socket.send("ACK")
    client_socket.close()

while True:

    client,addr = server.accept()
    
    print "[*] Accepted connection from: %s:%d" % (addr[0],addr[1])

    client_handler = threading.Thread(target=handle_client,args=(client,))

    client_handler.start()