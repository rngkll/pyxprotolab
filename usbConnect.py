import subprocess

def usbConnect():
    ''' 
    The function retrives the serial port which the device is connected.
    >>> usbConnect()
    the function returns something like that:   
    /dev/ttyUSB0
    '''
    val = ""
    command0 = 'sudo stty -F /dev/ttyUSB'
    for i in range(4):
        proc = subprocess.Popen(['/bin/bash'], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        command = ""
        command=command0+str(i)
        stdout=proc.communicate(command)
        if 'speed' in stdout[0]:
            val = '/dev/ttyUSB'+str(i)
            break
    
    if val == "":  
        print "The function does not recognize any device connected.\n Please try again."
        exit()
    else:
        print 'this is the usb connect to the xcope ',val
    return val
