from microbit import *

class mcp23017:
    def __init__(self, a = 0x20):
        self.ADD = a

    # BANK A=0 B=1
    def set_dir(self,bank,direction):
        data = bytes([bank,direction])
        i2c.write(self.ADD, data)

    def set_pull(self,bank,pull):
        data = bytes([bank + 0x0c,pull])
        i2c.write(self.ADD,data)

    def dig_write(self,bank,value):
        data = bytes([bank + 0x12,value])
        i2c.write(self.ADD,data)

    def dig_read(self,bank):
        buf = bytes([bank + 0x12])
        i2c.write(self.ADD,buf)
        return i2c.read(self.ADD,1)[0]

# test
p = mcp23017()
# set bank A to inputs
p.set_dir(0,0xff)
# set bank A to pullup
p.set_pull(0,0xff)
# set bank B to outputs
p.set_dir(1,0)
# turn bank B off
p.dig_write(1,0)

# test the leds
for i in range(8):
    p.dig_write(1,2**i)
    sleep(500)

# loop for reading buttons
while True:
    btns = p.dig_read(0)
    p.dig_write(1,btns^0xff)
    sleep(20)
