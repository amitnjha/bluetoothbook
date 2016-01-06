from bluetooth import *

server_address = "00:15:83:3D:0A:57"
port = 1

sock = BluetoothSocket(RFCOMM)

sock.connect((server_address,port))

sock.send("Hello from Pi v1 to v2")

sock.close()
