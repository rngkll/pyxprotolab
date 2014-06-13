#! /usr/bin/env python3

import serial
#import threading
#import time
import sys

#~ print serial.VERSION
if sys.version_info >= (3, 0):
    #print(sys.version_info)
    def data(string):
        return bytes(string, 'utf-8')
else:
    def data(string): return string 

class XprotolabController:
    '''Controller to manage de xprotolab'''

    def __init__(self):
        self.ser = serial.Serial()
        self.connect()

    def connect(self):
        self.ser.baudrate = 115200
        self.ser.port = '/dev/ttyUSB0'
        self.ser.bytesize = 8
        self.ser.parity = 'N'
        self.ser.stopbits = 1
        print("Connecting to", self.ser.name)

        self.ser.open()

        if self.ser.isOpen():
            print("Connected to port", self.ser.name)
        else:
            print("Can't connect to port")
            self.ser.close()

    def closeConnection(self):
        self.ser.close() 

    def show_version(self):
        self.ser.write(b'a')
        return self.ser.readline(4)

    def Request_CH1(self):
        self.ser.write(b'r')
        return self.ser.readline(256)

    def Request_CH2(self):
        self.ser.write(b's')
        return self.ser.readline(256)

    def Set_Post_Trigger_value(self)
        self.ser.write(b'j')
    
    def write_settings(self):
        self.ser.write(b'b')

    def restore_factory_settings(self):
        self.ser.write(b'k')

