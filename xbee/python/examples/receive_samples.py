#! /usr/bin/python

"""
receive_samples.py

By Paul Malmsten, 2010
pmalmsten@gmail.com

This example continuously reads the serial port and processes IO data
received from a remote XBee.
"""

from xbee import XBee
import serial

def toHex(s):
    lst = []
    for ch in s:
        hv = hex(ord(ch)).replace('0x', '')
        if len(hv) == 1:
            hv = '0'+hv
        hv = '0x' + hv
        lst.append(hv)

def decodeReceivedFrame(data):
            source_addr_long = toHex(data['source_addr_long'])
            source_addr = toHex(data['source_addr'])
            id = data['id']
            samples = data['samples']
            options = toHex(data['options'])
            return [source_addr_long, source_addr, id, samples]

PORT = '/dev/ttyUSB0'
BAUD_RATE = 9600

# Open serial port
ser = serial.Serial(PORT, BAUD_RATE)

# Create API object
xbee = XBee(ser)

# Continuously read and print packets
while True:
    try:
	print 'waiting'
	response = xbee.wait_read_frame()
	decodedData = decodeReceivedFrame(response)
        print decodedData
        #

        #print response
    except KeyboardInterrupt:
        break
        
ser.close()
