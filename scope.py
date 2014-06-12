#!/usr/bin/env python3
import serial

#declare serial port and configuration
#~ print(serial.VERSION)
ser = serial.Serial()
ser.baudrate = 115200
ser.port = '/dev/ttyUSB0'
ser.bytesize = 8
ser.parity = 'N'
ser.stopbits = 1

ser.open()
if ser.isOpen():
    print("Connected to port", ser.name)
#    print(bytearray('a','ascii')
    ser.write(b'r') #write only accepts bytes
    print(ser.readline(256)) #amount of bytes to read are in the xprotolab manual

else:
    ser.close()
#print(ser.readline())
