from luma.core.interface.serial import i2c, spi, pcf8574
from luma.core.interface.parallel import bitbang_6800
from luma.core.render import canvas
from luma.oled.device import ssd1306, ssd1309, ssd1325, ssd1331, sh1106, ws0010

import RPi.GPIO as GPIO
GPIO.setwarnings(False)


serial_i2c = i2c(port=1, address=0x3C)
serial_spi = spi(device=0, port=0)

# substitute ssd1331(...) or sh1106(...) below if using that device
device_i2c = sh1106(serial_i2c)
device_spi = ssd1306(serial_spi)

# with is een contextmanager die __enter__() en __exit__() methodes aanroept bi jstart en einde 

with canvas(device_spi) as draw:
    draw.rectangle(device_spi.bounding_box, outline="white", fill="black")
    draw.text((10, 40), ">Hello World SPI", fill="white")

with canvas(device_i2c) as draw:
    draw.rectangle(device_i2c.bounding_box, outline="white", fill="black")
    draw.text((10, 40), ">Hello World I2C", fill="white")