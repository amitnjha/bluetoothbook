#!/usr/bin/python


import sys
from bluetooth import *


service_matches = find_service ( name = "SampleServer", , uuid =  SERIAL_PORT_CLASS)

if len(service_matches) == 0:
    print "cant find service!"
    sys.exit(0)

first_match = service_matches[0]
port = first_match["port"]
name = first_match["name"]
host = first_match["host"]

print "Connecting to ", host

sock = BluetoothSocket(RFCOMM)
sock.connect((host,port))

sock.send("PyblueZ client says Hello!!")

data = sock.recv(80)
print "Got:: " , data

sock.close()



 

