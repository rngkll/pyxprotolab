#!/usr/bin/env python3
import serial
from usbConnect import usbConnect
import xprotolab_controller
test = xprotolab_controller.XprotolabController()
#Read Channel_CH1
print("Output Channel1: \n",test.Request_CH1())

#Read Channel_CH2
print('Output Channel2: \n',test.Request_CH2())

