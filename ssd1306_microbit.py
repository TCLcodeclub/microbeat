# SSD1306 driver for BBC micro:bit MicroPython (microbit.i2c)
# For 128x32 displays. Works on micro:bit v2 with the official micro:bit MicroPython.

from microbit import i2c, sleep

# 5x8 font for ASCII 32..127 (each char is 5 bytes, columns)
FONT = bytearray(
    b"\x00\x00\x00\x00\x00"  # space
    b"\x00\x00\x5F\x00\x00"  # !
    b"\x00\x07\x00\x07\x00"  # "
    b"\x14\x7F\x14\x7F\x14"  # #
    b"\x24\x2A\x7F\x2A\x12"  # $
    b"\x23\x13\x08\x64\x62"  # %
    b"\x36\x49\x55\x22\x50"  # &
    b"\x00\x05\x03\x00\x00"  # '
    b"\x00\x1C\x22\x41\x00"  # (
    b"\x00\x41\x22\x1C\x00"  # )
    b"\x14\x08\x3E\x08\x14"  # *
    b"\x08\x08\x3E\x08\x08"  # +
    b"\x00\x50\x30\x00\x00"  # ,
    b"\x08\x08\x08\x08\x08"  # -
    b"\x00\x60\x60\x00\x00"  # .
    b"\x20\x10\x08\x04\x02"  # /
    b"\x3E\x51\x49\x45\x3E"  # 0
    b"\x00\x42\x7F\x40\x00"  # 1
    b"\x42\x61\x51\x49\x46"  # 2
    b"\x21\x41\x45\x4B\x31"  # 3
    b"\x18\x14\x12\x7F\x10"  # 4
    b"\x27\x45\x45\x45\x39"  # 5
    b"\x3C\x4A\x49\x49\x30"  # 6
    b"\x01\x71\x09\x05\x03"  # 7
    b"\x36\x49\x49\x49\x36"  # 8
    b"\x06\x49\x49\x29\x1E"  # 9
    b"\x00\x36\x36\x00\x00"  # :
    b"\x00\x56\x36\x00\x00"  # ;
    b"\x08\x14\x22\x41\x00"  # <
    b"\x14\x14\x14\x14\x14"  # =
    b"\x00\x41\x22\x14\x08"  # >
    b"\x02\x01\x51\x09\x06"  # ?
    b"\x32\x49\x79\x41\x3E"  # @
    b"\x7E\x11\x11\x11\x7E"  # A
    b"\x7F\x49\x49\x49\x36"  # B
    b"\x3E\x41\x41\x41\x22"  # C
    b"\x7F\x41\x41\x22\x1C"  # D
    b"\x7F\x49\x49\x49\x41"  # E
    b"\x7F\x09\x09\x09\x01"  # F
    b"\x3E\x41\x49\x49\x7A"  # G
    b"\x7F\x08\x08\x08\x7F"  # H
    b"\x00\x41\x7F\x41\x00"  # I
    b"\x20\x40\x41\x3F\x01"  # J
    b"\x7F\x08\x14\x22\x41"  # K
    b"\x7F\x40\x40\x40\x40"  # L
    b"\x7F\x02\x0C\x02\x7F"  # M
    b"\x7F\x04\x08\x10\x7F"  # N
    b"\x3E\x41\x41\x41\x3E"  # O
    b"\x7F\x09\x09\x09\x06"  # P
    b"\x3E\x41\x51\x21\x5E"  # Q
    b"\x7F\x09\x19\x29\x46"  # R
    b"\x46\x49\x49\x49\x31"  # S
    b"\x01\x01\x7F\x01\x01"  # T
    b"\x3F\x40\x40\x40\x3F"  # U
    b"\x1F\x20\x40\x20\x1F"  # V
    b"\x3F\x40\x38\x40\x3F"  # W
    b"\x63\x14\x08\x14\x63"  # X
    b"\x07\x08\x70\x08\x07"  # Y
    b"\x61\x51\x49\x45\x43"  # Z
    b"\x00\x7F\x41\x41\x00"  # [
    b"\x02\x04\x08\x10\x20"  # backslash
    b"\x00\x41\x41\x7F\x00"  # ]
    b"\x04\x02\x01\x02\x04"  # ^
    b"\x40\x40\x40\x40\x40"  # _
    b"\x00\x01\x02\x04\x00"  # `
    b"\x20\x54\x54\x54\x78"  # a
    b"\x7F\x48\x44\x44\x38"  # b
    b"\x38\x44\x44\x44\x20"  # c
    b"\x38\x44\x44\x48\x7F"  # d
    b"\x38\x54\x54\x54\x18"  # e
    b"\x08\x7E\x09\x01\x02"  # f
    b"\x0C\x52\x52\x52\x3E"  # g
    b"\x7F\x08\x04\x04\x78"  # h
    b"\x00\x44\x7D\x40\x00"  # i
    b"\x20\x40\x44\x3D\x00"  # j
    b"\x7F\x10\x28\x44\x00"  # k
    b"\x00\x41\x7F\x40\x00"  # l
    b"\x7C\x04\x18\x04\x78"  # m
    b"\x7C\x08\x04\x04\x78"  # n
    b"\x38\x44\x44\x44\x38"  # o
    b"\x7C\x14\x14\x14\x08"  # p
    b"\x08\x14\x14\x18\x7C"  # q
    b"\x7C\x08\x04\x04\x08"  # r
    b"\x48\x54\x54\x54\x20"  # s
    b"\x04\x3F\x44\x40\x20"  # t
    b"\x3C\x40\x40\x20\x7C"  # u
    b"\x1C\x20\x40\x20\x1C"  # v
    b"\x3C\x40\x30\x40\x3C"  # w
    b"\x44\x28\x10\x28\x44"  # x
    b"\x0C\x50\x50\x50\x3C"  # y
    b"\x44\x64\x54\x4C\x44"  # z
    b"\x00\x08\x36\x41\x00"  # {
    b"\x00\x00\x7F\x00\x00"  # |
    b"\x00\x41\x36\x08\x00"  # }
    b"\x02\x01\x02\x04\x02"  # ~ (approx)
)

class SSD1306_I2C:
    def __init__(self, i2c_obj, width=128, height=32, addr=0x3C):
        self.i2c = i2c_obj
        self.width = width
        self.height = height
        self.addr = addr
        self.pages = self.height // 8
        self.buffer = bytearray(self.width * self.pages)
        self.init_display()

    def write_cmd(self, cmd):
        # control byte 0x00 for command
        i2c.write(self.addr, bytes([0x00, cmd]))

    def init_display(self):
        for cmd in (
            0xAE,             # DISPLAYOFF
            0xD5, 0x80,       # SETDISPLAYCLOCKDIV
            0xA8, self.height - 1,  # SETMULTIPLEX
            0xD3, 0x00,       # SETDISPLAYOFFSET
            0x40,             # SETSTARTLINE
            0x8D, 0x14,       # CHARGEPUMP (enable)
            0x20, 0x00,       # MEMORYMODE, Horizontal addressing
            0xA1,             # SEGREMAP (column addr 127 mapped to SEG0)
            0xC8,             # COMSCANDEC
            0xDA, 0x02 if self.height == 32 else 0x12,  # SETCOMPINS
            0x81, 0x7F,       # SETCONTRAST
            0xD9, 0xF1,       # SETPRECHARGE
            0xDB, 0x40,       # SETVCOMDETECT
            0xA4,             # DISPLAYALLON_RESUME
            0xA6,             # NORMALDISPLAY
            0x2E,             # DEACTIVATE_SCROLL
            0xAF              # DISPLAYON
        ):
            self.write_cmd(cmd)
            sleep(0)  # tiny yield

    def poweroff(self):
        self.write_cmd(0xAE)

    def poweron(self):
        self.write_cmd(0xAF)

    def contrast(self, contrast):
        self.write_cmd(0x81)
        self.write_cmd(contrast)

    def invert(self, invert):
        self.write_cmd(0xA7 if invert else 0xA6)

    def show(self):
        # Set column and page addresses then stream buffer in chunks
        self.write_cmd(0x21)  # set column address
        self.write_cmd(0)     # start column
        self.write_cmd(self.width - 1)  # end column
        self.write_cmd(0x22)  # set page address
        self.write_cmd(0)     # start page
        self.write_cmd(self.pages - 1)  # end page

        # send data in chunks (control byte 0x40)
        chunk = 16  # safe chunk size for micro:bit i2c
        buf_len = len(self.buffer)
        i = 0
        while i < buf_len:
            end = i + chunk
            if end > buf_len:
                end = buf_len
            # convert slice to bytes to avoid slice-assignment issues
            data = bytes(self.buffer[i:end])
            i2c.write(self.addr, bytes([0x40]) + data)
            i = end
            sleep(0)

    def pixel(self, x, y, color):
        if not (0 <= x < self.width and 0 <= y < self.height):
            return
        page = y // 8
        index = x + page * self.width
        mask = 1 << (y & 7)
        val = self.buffer[index]
        if color:
            val = val | mask
        else:
            val = val & (~mask & 0xFF)
        self.buffer[index] = val

    def fill(self, color):
        fill_byte = 0xFF if color else 0x00
        # assign element-wise for compatibility
        for i in range(len(self.buffer)):
            self.buffer[i] = fill_byte

    def text(self, string, x, y, color=1):
        # Basic text using 5x8 font. x,y in pixels. No clipping except bounds check.
        for ch in string:
            code = ord(ch)
            if code < 32 or code > 126:
                code = 32
            fi = (code - 32) * 5
            for col in range(5):
                if x >= self.width:
                    break
                col_byte = FONT[fi + col]
                for bit in range(8):
                    py = y + bit
                    if 0 <= py < self.height:
                        if (col_byte >> bit) & 1:
                            self.pixel(x, py, color)
                        else:
                            self.pixel(x, py, 0 if color else 1)
                x += 1
            # one column spacing
            if x < self.width:
                for bit in range(8):
                    py = y + bit
                    if 0 <= py < self.height:
                        self.pixel(x, py, 0 if color else 1)
            x += 1