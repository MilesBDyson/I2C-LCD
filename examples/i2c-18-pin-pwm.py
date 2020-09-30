#!/usr/bin/python3

import smbus
import time
import Adafruit_BBIO.PWM as PWM
from lcd_i2c import *

r = "P9_16"
g = "P9_14"
b = "P8_13"

PWM.start(r, 0, 1000, 1)
PWM.start(g, 0, 1000, 1)
PWM.start(b, 0, 1000, 1)
PWM.set_duty_cycle(r, 50)
PWM.set_duty_cycle(g, 30)
PWM.set_duty_cycle(b, 20)


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

    time.sleep(3)
except KeyboardInterrupt:
  pass
finally:
  lcd_byte(0x01, LCD_CMD)
  PWM.set_duty_cycle(r, 0)
  PWM.set_duty_cycle(g, 0)
  PWM.set_duty_cycle(b, 0)

  