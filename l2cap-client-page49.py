#!/usr/bin/python


from bluetooth import *

server_addr= "<>"

port = 0x1001

sock = BluetoothSocker(L2CAP)

sock.connect((server_addr,port))

sock.send("Hello!!")

sock.close()
