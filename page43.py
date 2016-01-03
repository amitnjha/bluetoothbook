#!/usr/bin/python
#example from page 43. Shows how to discover devices and print their name and 48 bit hex addresses.


from bluetooth import *
target_name = "My Phone"

target_address = None

print "Running discovery";

nearby_devices = discover_devices()


for  address in nearby_devices :
    print lookup_name(address), address;

