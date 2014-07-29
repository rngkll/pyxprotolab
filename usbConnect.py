import os

def usbConnect():
    ''' 
    The function retrives the serial port which the device is connected.
    >>> usbConnect()
    the function returns something like that:   
    /dev/ttyUSB0
    '''
    dir = "/dev"
    val = ""
    for i in os.listdir(dir):
        if i.find("ttyUSB") != -1:
            val = '/dev/'+i
            break
    
    if val == "":  
        print('The function does not recognize any device connected.\n Please try again')
        exit()
    else:
        print('this is the usb connect to the xcope ',val)
    return val

