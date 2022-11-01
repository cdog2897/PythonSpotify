from operations import Operations
import serial

import requests
import json
import time

# refresh token
# a = Operations()
# a.refreshAccessToken()




arduino = serial.Serial(port='/dev/cu.usbserial-0001', baudrate = 115200, timeout=.1)
while True:
	data = arduino.readline()
	if data:
	    print(data.decode('utf-8'))



    










