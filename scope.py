#!/usr/bin/env python3
import serial
import xprotolab_controller

test = xprotolab_controller.XprotolabController()

print(test.__doc__)
a = test.show_version()
print(a)
print(test.Request_CH1())
