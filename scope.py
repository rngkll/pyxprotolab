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
    print("Connected to port" + ser.name() )
    print(ser.name)
    ser.write('a')

else:
    ser.close()
#print(ser.readline())
