# Simple test for NeoPixels on Raspberry Pi
import time
import board
import neopixel
import RPi.GPIO as GPIO

#GPIO.setmode(GPIO.BOARD)
#GPIO.setup(18, GPIO.OUT)

# Choose an open pin connected to the Data In of the NeoPixel strip, i.e. board.D18
# NeoPixels must be connected to D10, D12, D18 or D21 to work.
pixel_pin = board.D18

# The number of NeoPixels
num_pixels = 2

# The order of the pixel colors - RGB or GRB. Some NeoPixels have red and green reversed!
# For RGBW NeoPixels, simply change the ORDER to RGBW or GRBW.
ORDER = neopixel.RGB

pixels = neopixel.NeoPixel(
    pixel_pin, num_pixels, brightness=0.5, auto_write=False, pixel_order=ORDER
)

print("begin")
while True:
    pixels.fill((0,255,0))
    print("running")
        #pixels[0] = (0,255,0)
        #pixels[1] = (0,0,0)
    pixels.show()
    time.sleep(0.01)

    