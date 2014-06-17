#!/usr/bin/env python3
import serial
import xprotolab_controller
from time import sleep
test = xprotolab_controller.XprotolabController()

print(test.__doc__)
#sleep(15)
print(test.show_version())
test.RequestSettings()
test.StopScope()
sleep(1)
test.StartScope()
#sleep(15)
print(serial.to_bytes([0x31, 0x0a, 0x32, 0x0a, 0x33, 0x0a]))
#print(b'17')
#print(bytes('17', 'utf-8'))
