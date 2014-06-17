#!/usr/bin/env python3
import serial
import xprotolab_controller
from time import sleep
test = xprotolab_controller.XprotolabController()

print(test.__doc__)
#sleep(15)
print(test.show_version())
print(test.RequestSettings())
test.write_settings()
test.StopScope()
sleep(5)
test.StartScope()
#sleep(15)
