# -*- coding: utf-8 -*
import serial
import time
import board
import neopixel

# Serial setup
ser = serial.Serial("/dev/ttyAMA0", 115200)

def get_tf_data_and_run_pixels():
    # Neopixel setup 
    pixel_pin = board.D18
    num_pixels = 2
    ORDER = neopixel.RGB
    pixels = neopixel.NeoPixel(pixel_pin,
        num_pixels, brightness=0.5, auto_write=False, pixel_order=ORDER)
    distance = 100    
    while True:
        #time.sleep(0.1)
        if distance < 20:
            pixels.fill((0,0,0))
        elif distance >20:
            pixels.fill((0,255,0))
        pixels.show()
        count = ser.in_waiting
        if count > 8:
            recv = ser.read(9)   
            ser.reset_input_buffer() 
            # type(recv), 'str' in python2(recv[0] = 'Y'), 'bytes' in python3(recv[0] = 89)
            # type(recv[0]), 'str' in python2, 'int' in python3 
            
            if recv[0] == 0x59 and recv[1] == 0x59:     #python3
                distance = recv[2] + recv[3] * 256
                strength = recv[4] + recv[5] * 256
                print('(', distance, ',', strength, ')')
                ser.reset_input_buffer()
                
            #if recv[0] == 'Y' and recv[1] == 'Y':     #python2
              #  lowD = int(recv[2].encode('hex'), 16)      
               # highD = int(recv[3].encode('hex'), 16)
                #lowS = int(recv[4].encode('hex'), 16)      
                #highS = int(recv[5].encode('hex'), 16)
                #distance = lowD + highD * 256
                #strength = lowS + highS * 256
                #print(distance, strength)
            
            # you can also distinguish python2 and python3: 
            #import sys
            #sys.version[0] == '2'    #True, python2
            #sys.version[0] == '3'    #True, python3


if __name__ == '__main__':
    try:
        if ser.is_open == False:
            ser.open()
        get_tf_data_and_run_pixels()
    except KeyboardInterrupt:   # Ctrl+C
        if ser != None:
            ser.close()

# Light neopixel
# Measure LiDAR Readings, check for success interrupt
# Stop neopixel and transmit signal to next pi
# Run receiver code