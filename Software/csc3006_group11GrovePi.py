#!/usr/bin/env python

import time
import grovepi
import math
import serial

# SIG,NC,VCC,GND
light_sensor = 0 # Connect the Grove Light Sensor to analog port A0

# SIG,NC,VCC,GND
dht_sensor = 2 # The Sensor goes on digital port 2.
dhtVal = 0 # The Blue colored sensor.

# Turn on once sensor exceeds threshold resistance
threshold = 300

grovepi.pinMode(light_sensor,"INPUT")
# grovepi.pinMode(led,"OUTPUT")

while True:
    ser = serial.Serial('/dev/ttyACM1', 9600, timeout=1)
    ser.flush()
    try:
            # Phototransistor
            # Get sensor value
            lightVal = grovepi.analogRead(light_sensor)
            
            # Calculate uv dose
            dose = lightVal * 30 #for the purpose of this project we will indicate the time as 30sec
            if (x <= 0):
                resistance = 0
            else:
                resistance = (float)(1023 - lightVal) * 10 / lightVal
            
            if dose < threshold:
                print("STERILISED")
                # Send HIGH to switch on LED
            else:
                # Send LOW to switch off LED
                print("NOT STERILISED")
            print("lightVal = %d resistance = %0.2f" %(lightVal,  resistance))
            time.sleep(2)

    except IOError:
        # send error message to arduino
        print("Phototransistor Error!")
        
        ser.write(b"Phototransistor Error\n")
        line = ser.readline().decode('utf-8').rstrip()
        print(line)
        time.sleep(20)
    try:
        # DHT11
        # The first parameter is the port, the second parameter is the type of sensor
            [temp,humidity] = grovepi.dht(dht_sensor,dhtVal)
            humidity = 73
            if humidity < 80:
                print ("DRY")
            else:
                print ("NOT DRY")
            
            if math.isnan(temp) == False and math.isnan(humidity) == False:
                print("temp = %0.2f c humidity = %0.2f%%"%(temp,humidity))
            time.sleep(2)
    except IOError:
        # send error message to arduino
        print("DHT11 Error!")
        ser.write(b"DHT11 Error\n")
        line = ser.readline().decode('utf-8').rstrip()
        print(line)
        time.sleep(20)                                                                                                  