I2C Enabled LCD Screen
=======================

Python code that will allow you use an I2C Backpack connected to a wide
range of LCD screens on a Beaglebone Black.

the I2C Backpack works with the 18pin RGB Char Displays as well,
all pins line up except pin16(gnd) on the Backpack and is not used
at all leaving the last 3 pins on the RGB display free for PWM
or gpio connections and will be controlled seperatly from the Backpack.

Pinouts of bothe the 16pin and 18pin displays are included in the
images file for your review as well as examples for controlling both
displays are included in the examples folder as well.

[Wiki](https://github.com/MilesBDyson/I2C-LCD/wiki)

| Board pin name | Board pin | Beaglebone Black pin name |
|----------------|-----------| --------------------------|
| SCL            | 1         | P9\_19, I2C2\_SCL         |
| SDA            | 2         | P9\_20, I2C\_SDA          |
| VCC            | 3         | P9\_5, VDD\_5v            |
| GND            | 4         | P9\_1, Ground             |

![Backpack1](images/i2c_backpack.jpg)
![Backpack2](images/i2c_enabled_lcd.jpg)
