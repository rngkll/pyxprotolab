#!/usr/bin/env python3
import serial
import xprotolab_controller
test = xprotolab_controller.XprotolabController()
#import matplotlib.pyplot as plt

#reset factory default settings
print("Firmware version: ",test.show_version())
test.restore_factory_settings()
test.RequestSettings()

#Read Channel_CH1
print("Output Channel1: \n",test.Request_CH1())

#Read Channel_CH2
print('Output Channel2: \n',test.Request_CH2())

#plt.plot([1,2,3,4])
#plt.ylabel('some numbers')
#plt.show()

