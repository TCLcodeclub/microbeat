
from microbit import i2c

class Mcp23017:
    def __init__(self, a = 0x20):
        """
        Initialize MCP23017 chip at address 0x20
        
        :Param a = address
        
        """
        self.ADD = a

    # BANK A=0 B=1
    
    def set_io_direction(self,bank,direction):
        """
        Set IO direction for IO bank
        
        :param bank: 0 = bank A, 1 = bank B
        :param direction: Byte, 1  = input, 0 = output
        """
        data = bytes([bank,direction])
        i2c.write(self.ADD, data)

    def set_io_pullups(self,bank,pullup):
        """
        Enable pull-up resistors for IO bank
        
        :param bank: 0 = bank A, 1 = bank B
        :param pull: Byte, bit set to 1 pullup, bit set to 0 no pullup
        """
        data = bytes([bank + 0x0c,pullup])
        i2c.write(self.ADD,data)

    def io_write(self,bank,value):
        """
        Write pin values to IO bank
        
        :param bank: 0 = bank A, 1 = bank B
        :param value: Byte, bit set 1 - VDD , bit set to 0 - OV
        """
        data = bytes([bank + 0x12,value])
        i2c.write(self.ADD,data)

    def io_read(self,bank):
        """
        Returns byte representing levels on IO pin for bank
        
        :param bank: 0 = bank A, 1 = bank B
        """
        buffer = bytes([bank + 0x12])
        i2c.write(self.ADD,buffer)
        return i2c.read(self.ADD,1)[0]

