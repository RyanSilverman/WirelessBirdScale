#! /usr/bin/python3

import datetime
import time
import sys
import Adafruit_DHT
import csv
from picamera import PiCamera
import numpy as np

# -------------CVS-----------------------
csv_file = "Data/readings.csv"
#--------------CAMERA--------------------
camera = PiCamera()
camera.resolution = (3280, 2464)
# -------------AMPLIFIER-----------------
EMULATE_HX711=False
referenceUnit = 866.835398  # This was set during the calibration process of the HX711 amplifier

if not EMULATE_HX711:
    import RPi.GPIO as GPIO
    from hx711 import HX711
else:
    from emulated_hx711 import HX711

def cleanAndExit():
    print("Cleaning...")

    if not EMULATE_HX711:
        GPIO.cleanup()
        
    print("Exitting...")
    sys.exit()

hx = HX711(5, 6) # Setting the pins to GPIO 5 and GPIO 6 for the amplifier
hx.set_reading_format("MSB", "MSB")
hx.set_reference_unit(referenceUnit) # Calibrating the amplifier
hx.reset()
hx.tare()
print("Scale has been zeroed! Ready to measure bird's weight")

#--------------Temp and Humidity---------
DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 4
# ---------------------------------------

def write_to_csv(weight, temperature, humidity, csv_file, timestamp = None):
    
    # Open the CSV file in append mode
    with open(csv_file, "a", newline="") as file:
        writer = csv.writer(file)
        #If the time has been specified then add it to the row, else omit it
        if(timestamp==None):
            # Write the data as a new row in the CSV file
            writer.writerow([weight, temperature, humidity])
        else:
            # Write the data as a new row in the CSV file
            writer.writerow([timestamp, weight, temperature, humidity])
        
        print("Written to", csv_file)

# Temporary weight value buffer
weight_arr = []

while True:
    try:
	# Read the weight value from the load cell. Sometimes it yields  slightly negative values, thus make the minimum value 0.
        val = max(0, hx.get_weight(5))

        print("Weight reading:",format(val, ".2f"))

	# Only record the weight value if it is greater than 30 grams or less than 80 grams to
        # account for any leaves or light objects that may land on the load cell and for large impulses generated
	# by the bird landing and moving on the scale. i.e. discard small and large readings
        if(val >= 30 and val<=80):
            # Get the current local date and time
            current_time = datetime.datetime.now()
            # Format the current time as a string
            formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
	    # Name the image according to the timestamp
            camera.capture('Data/{}.jpg'.format(formatted_time))
            print("Image taken!")
            # Add the weight value to the temporary weight array
            weight_arr.append(val)

	# If there are weight values buffered in the weight array
        elif(len(weight_arr) != 0):
		# Calculate the average of the weights
                avg_weight = np.mean(weight_arr)
                print("The average weight of the bird is:",avg_weight)

                # Get the current local date and time
                current_time = datetime.datetime.now()
                # Format the current time as a string
                formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
		# Get thr temperature and humidity values from the DHT22 sensor
                humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
                # Write the average weight, temperature, humidity and timestamp to the CSV file
                write_to_csv(format(avg_weight, ".2f"), format(temperature, ".2f"), format(humidity, ".2f"), csv_file ,formatted_time)
		# Clear the temporary weight buffer for the next time the bird lands on the scale
                weight_arr.clear()

	# Power cycle the amplifier
        hx.power_down()
        hx.power_up()

    except (KeyboardInterrupt, SystemExit):
        cleanAndExit()
    except Exception as e:
        print(e)
        cleanAndExit()
