#!/usr/bin/python

import smbus
import time
import Adafruit_BBIO.GPIO as GPIO
from lcd_i2c import *

r = "P8_7"
g = "P8_9"
b = "P8_11"

GPIO.setup(r, GPIO.OUT)
GPIO.setup(g, GPIO.OUT)
GPIO.setup(b, GPIO.OUT)


# set to 0 the color you wish to be on
# red 	= 0 1 1
# green 	= 1 0 1
# blue 	= 1 1 0
# purple = 0 1 0
# CYAN   = 1 0 0

GPIO.output(r, 1)
GPIO.output(g, 1)
GPIO.output(b, 0)

# Main program block

# Initialise display
lcd_init()
try:
  while True:
  	 
    # Send some test
    lcd_string("Beaglebone Black",LCD_LINE_1)
    lcd_string("I2C LCD            <",LCD_LINE_2)

    time.sleep(3)

    # Send some more text
    lcd_string("Beaglebone Black",LCD_LINE_1)
    lcd_string(">            I2C LCD",LCD_LINE_2)

    time.sleep(3)
    lcd_byte(0x01,LCD_CMD)
    time.sleep(3)
except KeyboardInterrupt:
  pass
finally:
  lcd_byte(0x01, LCD_CMD)