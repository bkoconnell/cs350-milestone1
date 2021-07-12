#!/usr/bin/env python
#
# GrovePi Example for using the Grove Temperature & Humidity Sensor Pro 
# (http://www.seeedstudio.com/wiki/Grove_-_Temperature_and_Humidity_Sensor_Pro)
#
# The GrovePi connects the Raspberry Pi and Grove sensors.  
# You can learn more about GrovePi here:  http://www.dexterindustries.com/GrovePi
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
import grovepi
import math
# import json
import json
# import grove_rgb_lcd, sleep, and isnan
from grove_rgb_lcd import *
from time import sleep
from math import isnan

# Connect the Grove Temperature & Humidity Sensor Pro to digital port D4
# This example uses the blue colored sensor.
# SIG,NC,VCC,GND
sensor = 7  # The Sensor goes on digital port 7.

# temp_humidity_sensor_type
# Grove Base Kit comes with the blue sensor.
blue = 0    # The Blue colored sensor.

while True:
    try:
        # This example uses the blue colored sensor. 
        # The first parameter is the port, the second parameter is the type of sensor.
        [temp,humidity] = grovepi.dht(sensor,blue)  
        if math.isnan(temp) == False and math.isnan(humidity) == False:
            # send data to json file
            tempF = (temp * 1.8) + 32
            data = {'Temp': "%.02f F"%(tempF), 'Humidity': "%.02f%%"%(humidity)}
            with open('data.json', 'a+', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=4)
            print(data)
            
            # convert float to string for LCD output
            t = str(tempF)
            h = str(humidity)
            
            # display formatted data on LCD screen
            setText_norefresh("T:" + t + "F\n" + "H:" + h + "%")


    except (IOError, TypeError) as e:
        print(str(e))
        # and since we got a type error
        # then reset the LCD's text
        setText("")

    except KeyboardInterrupt as e:
        print(str(e))
        # since we're exiting the program
        # it's better to leave the LCD with a blank text
        setText("")
        break

    # wait some time before re-updating the LCD
    sleep(0.05)