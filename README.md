Garmin Vívosmart HR and GNU/Linux
=================================

There is no official GNU/Linux support from Garmin for the Vívosmart HR watch. However, it is possible to access the device in USB mass storage mode and retrieve the log files. Unlike some similar devices, no synchronization of your data with the cloud is necessary – you can also access your data completely without internet connection.

At least with my firmware version (4.00), the device does not get recognized automatically as a mass storage device. This is the output from dmesg:

```
usb X-X: new full-speed USB device number X using uhci_hcd
usb X-X: device not accepting address X, error -71
usb X-X: new full-speed USB device number X using uhci_hcd
usb X-X: New USB device found, idVendor=091e, idProduct=0003
usb X-X: New USB device strings: Mfr=0, Product=0, SerialNumber=0
```

To get it recognized and mounted, it is necessary to send the command `0x140000002f0400000100000000` to the device, over USB "Bulk out" (endpoint number 3). For this, you can use the python script `send_command.py`:

```
sudo python ./send_command.py
```

The script depends on pyusb (package `python-usb` / `python3-usb` in Debian and Ubuntu). It may be necessary to [blacklist the garmin_gps kernel module][osmwiki]. To use the script without sudo, you need to add an [udev rule][osmwiki].

The log files in FIT format can be retrieved from the folders `GARMIN/ACTIVITY` and `GARMIN/MONITOR`. There are several GUI applications with partial support for FIT files, e.g. GoldenCheetah, pytrainer and turtlesport.

The perl library [Garmin::FIT][garminfit] can be used to parse FIT files and also comes with a very useful script called `fitdump.pl` that converts to a human-readable text format.

[osmwiki]: http://wiki.openstreetmap.org/wiki/USB_Garmin_on_GNU/Linux
[garminfit]: https://github.com/mrihtar/Garmin-FIT
