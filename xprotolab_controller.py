#! /usr/bin/env python3

import serial
#import threading
#import time
import sys

#~ print serial.VERSION
if sys.version_info >= (3, 0):
    #print(sys.version_info)
    def data(string):
        return bytes(string, 'latin1')
else:
    def data(string): return string 

class XprotolabController():
    '''Controller to manage de xprotolab'''

    def __init__(self):
        self.connect

    def connect(self):
        print("Connecting to", self.ser.name)
        self.ser = serial.Serial()
        self.ser.baudrate = 115200
        self.ser.port = '/dev/ttyUSB0'
        self.ser.bytesize = 8
        self.ser.parity = 'N'
        self.ser.stopbits = 1

        self.ser.open()

        if ser.isOpen():
            print("Connected to port", self.ser.name)
       
        else:
            print("Can't connect to port")
            self.ser.close()

    def closeConnection(self):
        self.ser.close() 

    def show_version(self):
        self.ser.write(b'a')
        return self.ser.readline(4)

    def write_settings(self):
        self.ser.write(b'b')

    def restore_factory_settings(self):
        self.ser.write(b'k')


