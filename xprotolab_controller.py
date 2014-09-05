#! /usr/bin/env python3

import serial
#import threading
#import time
import sys
from usbConnect import usbConnect

#~ print(serial.VERSION)
if sys.version_info >= (3, 0):
    def data(string):
        return bytes(string, 'utf-8')
        #return serial.to_bytes(string)
else:
        def data(string): return string 

class XprotolabController:
    '''Controller to manage de xprotolab'''

    def __init__(self):
        self.ser = serial.Serial()
        self.connect()

    def connect(self):
        self.ser.baudrate = 115200
        self.ser.port = usbConnect()
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
        return self.ser.readline(4)

    def RequestSettings(self):
        self.ser.write(data('u'))
        for byte in self.ser.readline(43):
            print(byte)
        #print("Channel 1 settings:")
        #print("Channel Position: ",self.ser.readline(1))
        #print("Bitfield: ",self.ser.readline(1))
        #print("Channel Gain: ",self.ser.readline(1))
        #
        #print("Channel 2 settings:")
        #print("Channel Position: ",self.ser.readline(1))
        #print("Bitfield: ",self.ser.readline(1))
        #print("Channel Gain: ",self.ser.readline(1))

        #print("Channel D settings:")
        #print("Channel Position: ",self.ser.readline(1))
        #print("Input mask: ",self.ser.readline(1))
        #print("Option: ",self.ser.readline(1))
        #print("Decode parameter: ",self.ser.readline(1))
        #print("Decode option: ",self.ser.readline(1))

        #print("General settings: ",self.ser.readline(10))
        #
        #print("AWG settings: ",self.ser.readline(8))
        #print("Extras: ",self.ser.readline(14))

    def Request_CH1(self):
        self.ser.write(data('r'))
        return self.ser.readline(256)

    def Request_CH2(self):
        self.ser.write(data('s'))
        return self.ser.readline(256)

    def increaseCH1gain(self):
        self.ser.write(data('7'))

    def StopScope(self):
        self.ser.write(data('f'))

    def StartScope(self):
        self.ser.write(data('g'))

    def Set_Post_Trigger_value(self):
        self.ser.write(data('j'))

    def write_settings(self):
        self.ser.write(data('b78'))

    def restore_factory_settings(self):
        self.ser.write(data('k'))

