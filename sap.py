#program started in startup. captures signals and initiates and kills camera according to signal
#
#Author: Buddhika De Seram

import sys
import os
from capture import *
import subprocess
import signal
import shlex
import errno
import RPi.GPIO as gpio
import time, commands

def signal_handle(signal, frame):
    capture.terminate()
    if capture.wait() != None:
        sys.exit(0)

vid = commands.getoutput('ls /dev |grep video')
camera = int(vid[-1])
counter = 0
poll = 1
initfile = 'CAPTURE.txt'
endfile = "ENDCAPTURE.txt"
end = "__COMPLETE__(CAPTURE)"
init = "__INIT__(CAPTURE)"
path= '/home/pi/sap/control/'
while poll:
    gpio.cleanup()
    signal.signal(signal.SIGINT, signal_handle)
    for file in os.listdir(path):

        #checks if filename is in correct format
        if file == initfile:
            file = open(path + initfile, 'r')
            x= file.readline()[:-2]

            #Check if first line is in correct format
            if x == init:
                date = file.readline()[:-2]
                counter+=1  #day counter
                foldername = "/home/pi/sap/data/" + date + 'No' + str(counter)

                #Creates new folder in /home/pi/SAP/data 
                while True:
                    try:
                        os.mkdir(foldername)
                        break
                    except OSError, e:
                        if e.errno == errno.EEXIST:
                            #file already exists
                            counter += 1 
                            foldername = "/home/pi/sap/data/" + date + 'No' + str(counter)
                            print foldername
                        else:
                            #unknown error
                            sys.exit(1)
                file.close()
               
                #deletes the initiate file
                os.remove(path + initfile)
                loop = 1

                #starts camera and saves images in folder /home/pi/SAP/data/*date + 'No' + counter*
                
                arg = "/usr/bin/python ./capture.py "+ foldername + " " + str(camera)
                args = shlex.split(arg)
                capture = subprocess.Popen(args)
                while loop:
                    #checks for end signal from main computer:
                    for file in os.listdir(path):
                        if file == endfile:
                            file = open(path + endfile, 'r')
                            line = file.readline()
                            if line == end:
                                loop = 0
                                os.remove(path + endfile)
                                capture.terminate()
                                if os.listdir(foldername) == []:
                                    os.removedirs(foldername)
                                 
