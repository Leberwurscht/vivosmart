#!/usr/bin/env python

import sys, usb.core, binascii

dev = usb.core.find(idVendor=0x091e, idProduct=0x0003)
if dev is None: sys.exit("No Garmin found in the system");

try:
  if dev.is_kernel_driver_active(0) is True: dev.detach_kernel_driver(0)
except usb.core.USBError as e:
  sys.exit("Kernel driver won't give up control over device: %s" % str(e))

try:
    dev.set_configuration()
    dev.reset()
except usb.core.USBError as e:
    sys.exit("Cannot set configuration the device: %s" % str(e))

endpoint = dev[0][(0,0)][2]
data = binascii.unhexlify('140000002f0400000100000000')
dev.write(endpoint.bEndpointAddress, data)

print "Command sent."
