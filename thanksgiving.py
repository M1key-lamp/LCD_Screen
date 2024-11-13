import time
import gc
import board
import displayio
import random
from adafruit_st7789 import ST7789
from adafruit_display_shapes.circle import Circle
from adafruit_display_shapes.rect import Rect
from adafruit_display_shapes.polygon import Polygon

# Constants
PUMPKIN_CENTER_X = 120
PUMPKIN_CENTER_Y = 100
PUMPKIN_RADIUS = 25
PUMPKIN_OFFSET = 7
STEM_OFFSET = 48
STEM_WIDTH = 12
STEM_HEIGHT = 24
MOON_X = 20
MOON_Y = 30
MOON_RADIUS = 10
CRESENT_OFFSET = 5
LIGHTNING = [(180, 0), (165, 40), (170, 40), (166, 60), (185, 30), (175, 30), (190, 0)]

# Colors
PUMPKIN = 0xFFAA00
BACKGROUND = 0XFFFFF
MOON = 0xCCCC00
STEM = 0x00AA00
WHITE = 0xFFFFFF
HEAD = 0x964B00


displayio.release_displays()

spi = board.SPI()
tft_cs = board.D2
tft_dc = board.D3

dbus = displayio.FourWire(spi, command=tft_dc, chip_select=tft_cs)
display = ST7789(dbus, rotation=270, width=240, height=135, rowstart=40, colstart=53)


# Make the display context
main_group = displayio.Group()

# Make a background color fill
color_bitmap = displayio.Bitmap(display.width, display.height, 3)
color_palette = displayio.Palette(5)
color_palette[0] = BACKGROUND
color_palette[1] = PUMPKIN
color_palette[2] = MOON
color_palette[3] = STEM
color_palette[4] = WHITE
bg_sprite = displayio.TileGrid(color_bitmap, pixel_shader=color_palette, x=0, y=0)
main_group.append(bg_sprite)
display.root_group= main_group
# Draw Pumpkin (Created from 3 circles and rectangle)

cresent = Circle(MOON_X, MOON_Y, MOON_RADIUS, fill=MOON)
main_group.append(cresent)
shadow = Circle(MOON_X - CRESENT_OFFSET, MOON_Y - CRESENT_OFFSET, MOON_RADIUS, fill=BACKGROUND)
main_group.append(shadow)

# Lightning


#circle

feathers1 = RoundRect(60, 40, 101, 60, 30, fill= 0xFFFF00)
main_group.append(feathers1)

feathers2 = RoundRect(80, 40, 101, 60, 30, fill= 0x8B0000)
main_group.append(feathers2)

BODY = Circle(120, 80, 40, fill= 0x964B00, outline = 0xFFFFFF)
main_group.append(BODY)

HEAD =  Circle(120, 40, 20, fill= 0x964B00, outline = 0xFFFFFF)
main_group.append(HEAD)

EYE1 =  Circle(110, 40, 10, fill= 0xFFFFFF, outline = 0xFFFFFF)
main_group.append(EYE1)


EYE2 =  Circle(130, 40, 10, fill= 0xFFFFFF, outline = 0xFFFFFF)
main_group.append(EYE2)

Pupil1=  Circle(130, 40, 8, fill= 0x00000, outline = 0xFFFFFF)
main_group.append(Pupil1)

Pupil2 =  Circle(110, 40, 8, fill= 0x00000, outline = 0xFFFFFF)
main_group.append(Pupil2)


Feet1 =Rect(100,120, 25, 10, fill= 0xFFA500)
main_group.append(Feet1)

Feet2 =Rect(118,120, 25, 10, fill= 0xFFA500)
main_group.append(Feet2)


count = 0
direction = 1
while True:
   pass
