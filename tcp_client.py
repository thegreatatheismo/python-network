#!/usr/bin/python

import socket

target_host = raw_input("Enter an IP Address: ")
target_port = int(raw_input("Enter a Port: "))

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((target_host,target_port))

client.send("GET / HTTP/1.1\r\nHost: (%s)\r\n\r\n" % target_host)

response = client.recv(4096)

print response
