#!/usr/bin/env python3
import matplotlib.pyplot as pl
#import serial
import xprotolab_controller
#Importing the modules: matplotlib, serial and Xprotolab_controller
test = xprotolab_controller.XprotolabController()
'''
The code, attempts to draw a graphic of the wave, taking data from the 
output of the xprotolab device

'''

#dataControl Function
def dataControl(i,zoom=None):
    '''
    The function takes the data from the device and applies a format to interprete
    the data that will be use to draw the graphic
    Data interpretation:
    The output is format 0 - 256, to draw a wave, the function needs nagative and positive data.
    256 = peek +
    128 = 0
    0   = peek -
    dataControl(200)
    5
    '''
    if zoom is None:
        zoom=10
    if i == 128:
        a = 0
    elif i > 128:
        a = ((i - 128) * zoom) / 128
    else:
        a = -((128 - i) * zoom) / 128
    return int(a)

print("Firmware version: ",test.show_version())
test.restore_factory_settings()
l = test.RequestSettings()
print(l)
zoom = 100
action = input("Please enter the mode (Scope or Meter)\n")
if action == "Scope":
    #Read Channel_CH1
    valCH1=test.Request_CH1()
    #Read Channel_CH2
    valCH2=test.Request_CH2()
    CH1 = []
    CH2 = []
    for i in valCH1:
        CH1.append(dataControl(i,zoom))
    
    for i in valCH2:
        CH2.append(dataControl(i,zoom))
    
    pl.plot(CH1)
    pl.plot(CH2)
    pl.ylabel('Values of test.py')
    pl.xlabel('Numbers')
    pl.show()

elif action == "Meter":
    #Read Channel_CH1
    valCH1=test.Request_CH1()
    CH1 = []
    
    for i in valCH1:
        CH1.append(dataControl(i))
    
    pl.plot(CH1)
    pl.ylabel('Voltage')
    pl.xlabel('Times')
    pl.show()

else:
    print("This action is not valid, Try again")
    exit()
