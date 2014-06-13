#! /usr/bin/env python3

import serial
#import threading
#import time
import sys

#~ print(serial.VERSION)
if sys.version_info >= (3, 0):
    def data(string):
        return bytes(string, 'latin1')
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
        self.ser.write(data('a'))
        print(serial.to_bytes([0x31, 0x0a, 0x32, 0x0a, 0x33, 0x0a]))
        return self.ser.readline(4)

    def RequestSettings(self):
        self.ser.write(data('u'))
        return self.ser.readline(44)

    def Request_CH1(self):
        self.ser.write(data('r'))
        return self.ser.readline(256)

    def Request_CH2(self):
        self.ser.write(data('s'))
        return self.ser.readline(256)

    def StopScope(self):
        self.ser.write(data('f'))

    def StartScope(self):
        self.ser.write(data('g'))

    def Set_Post_Trigger_value(self):
        self.ser.write(data('j'))

    def write_settings(self):
        self.ser.write(data('b78'))
        #self.ser.write(data(index))
        #self.ser.write(data(data))

    def restore_factory_settings(self):
        self.ser.write(data('k'))

