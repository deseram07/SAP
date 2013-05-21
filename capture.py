import cv
import cv2
import sys, os,subprocess
import RPi.GPIO as gpio
import time
import signal
import os
# setting up gpio pins

def signal_handler(signal, frame):
    gpio.cleanup()
    sys.exit(0)

def main(argv):
    imagename = "cap"
    ext = ".jpg"
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)
    cap = 15
    flash = 7
    led_bz = 22
    led_ready = 16
    ur_laser = 12
    ll_laser = 11
    lr_laser = 13
    lasers = [flash, ur_laser, ll_laser, lr_laser]
    foldername = argv[0]
    camera = int(argv[1])
    index = 0
    print foldername
    os.chdir(foldername)
    
    #initiate pins
    gpio.setmode(gpio.BOARD)
    gpio.setup(cap, gpio.IN, gpio.PUD_DOWN)
    gpio.setup(flash, gpio.OUT)
    gpio.setup(led_bz, gpio.OUT)
    gpio.setup(led_ready, gpio.OUT)

    #targeting lasers
    for i in lasers:
        gpio.setup(i, gpio.OUT)
        gpio.output(i, True)

    capture = cv2.VideoCapture(camera)
    capture.set(cv.CV_CAP_PROP_FRAME_WIDTH, 1920)
    capture.set(cv.CV_CAP_PROP_FRAME_HEIGHT, 1080)
    while 1:
        for i in lasers:
            gpio.output(i,True)
        gpio.output(led_ready, True)
        gpio.output(led_bz, False)
        
        f,image = capture.read()
        if gpio.input(cap):
            gpio.output(led_ready, False)
            gpio.output(led_bz, True)
            for i in lasers:
                gpio.output(i, False)
            filename = imagename + str(index) + ext 
            cv2.imwrite(filename, image)
            index += 1
            time.sleep(5)
        signal.signal(signal.SIGINT, signal_handler)
        signal.signal(signal.SIGTERM, signal_handler)
    gpio.cleanup()

if __name__ == "__main__":
    main(sys.argv[1:])
