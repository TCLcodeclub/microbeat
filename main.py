# Example usage for micro:bit v2 with 128x32 SSD1306
from microbit import i2c, sleep
from ssd1306_microbit import SSD1306_I2C

# If your display uses address 0x3D change addr below
oled = SSD1306_I2C(i2c, width=128, height=32, addr=0x3C)

oled.fill(0)
oled.text("Hello, micro:bit!", 0, 0)
oled.text("SSD1306 128x32", 0, 10)
# draw some pixels / pattern
for x in range(0, 128, 4):
    for y in range(20, 28):
        oled.pixel(x, y, 1)
oled.show()

while True:
    # simple toggle invert every 2 seconds
    sleep(2000)
    oled.invert(True)
    oled.show()
    sleep(2000)
    oled.invert(False)
    oled.show()