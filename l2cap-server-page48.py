#!/usr/bin/python

from bluetooth import *

port =  0x1001

backlog = 1

server_sock = BluetoothSocker(L2CAP)

server_sock.bind(("",port))

client_sock,address = server_sock.accept()

print "Accepted Connection from " , address

data = client_sock.recv(1024)
print "recieved [%s]" % data

client_sock.close()
server_sock.close()

