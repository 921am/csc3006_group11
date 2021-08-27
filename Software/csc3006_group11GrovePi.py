#!/usr/bin/env python
#
# GrovePi Example for using the Grove Light Sensor and the LED together to turn the LED On and OFF if the background light is greater than a threshold.
# Modules:
# 	http://www.seeedstudio.com/wiki/Grove_-_Light_Sensor
# 	http://www.seeedstudio.com/wiki/Grove_-_LED_Socket_Kit
#
# The GrovePi connects the Raspberry Pi and Grove sensors.  You can learn more about GrovePi here:  http://www.dexterindustries.com/GrovePi
#
# Have a question about this example?  Ask on the forums here:  http://forum.dexterindustries.com/c/grovepi
#
'''
## License

The MIT License (MIT)

GrovePi for the Raspberry Pi: an open source platform for connecting Grove Sensors to the Raspberry Pi.
Copyright (C) 2017  Dexter Industries

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
'''

import time
import grovepi
import math

# SIG,NC,VCC,GND
light_sensor = 0 # Connect the Grove Light Sensor to analog port A0

# SIG,NC,VCC,GND
buzzer = 3
dht_sensor = 2 # The Sensor goes on digital port 2.
dhtVal = 0 # The Blue colored sensor.

# Turn on once sensor exceeds threshold resistance
threshold = 10

grovepi.pinMode(light_sensor,"INPUT")
# grovepi.pinMode(led,"OUTPUT")

while True:
	try:
		#Phototransistor
		# Get sensor value
		lightVal = grovepi.analogRead(light_sensor)
		
		# Calculate resistance of sensor in K
		resistance = (float)(1023 - lightVal) * 10 / lightVal
		
		#if resistance > threshold:
		    # Send HIGH to switch on LED
		    
		#else:
		    # Send LOW to switch off LED
		    
		
		print("lightVal = %d resistance = %.2f" %(lightVal,  resistance))
		time.sleep(.5)

	except IOError:
		#activate buzzer
		grovepi.digitalWrite(buzzer,1)
		print("Phototransistor Error!")
		time.sleep(1)
		grovepi.digitalWrite(buzzer,0)
		time.sleep(5)

	try:
		#DHT11
		#The first parameter is the port, the second parameter is the type of sensor
	        [temp,humidity] = grovepi.dht(dht_sensor,dhtVal)
	        if math.isnan(temp) == False and math.isnan(humidity) == False:print("temp = %0.2f c humidity = %0.2f%%"%(temp,humidity))
	except IOError:
		#activate buzzer
		grovepi.digitalWrite(buzzer,1)
		print("DHT11 Error!")
		time.sleep(1)
		grovepi.digitalWrite(buzzer,0)
		time.sleep(5)