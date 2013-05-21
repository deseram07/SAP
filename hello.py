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
    cap = 15
    flash = 7
    led_bz = 16
    led_ready = 22
    ur_laser = 12
    ll_laser = 11
    lr_laser = 13
    lasers = [flash, ur_laser, ll_laser, lr_laser]
    foldername = argv[1]
    count = argv[2]
    camera = int(argv[3])

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
    while i:
        gpio.output(led_ready, True)
        gpio.output(led_bz, False)
        f,image = capture.read()
        if gpio.input(cap):
            gpio.output(led_ready, False)
            gpio.output(led_bz, True)
            for i in lasers:
                gpio.output(i, False)
            cv2.imwrite('cap.jpg', image)
            time.sleep(5)
    	    break
        signal.signal(signal.SIGINT, signal_handler)
        signal.signal(signal.SIGTERM. signal_handle)
    gpio.cleanup()

if __name__ == "__main__":
    main(sys.argv[1:])
