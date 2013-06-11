These files are required to be stored in the Raspberry Pi which handles the communication 
between the main computer and camera system. This is used to control the camera and pull 
the images from the Raspberry Pi to the main computer.

The files needs to be saved in the home directory in a folder called ‘sap’
“/home/pi/sap”

In this folder, two directories must be created called ‘control’ and ‘data’. 
Control signals are received in the ‘control’ folder while the images are 
stored in the ‘data’ folder. This can be done using the function:

“sudo mkdir /home/pi/sap/control”
“sudo mkdir /home/pi/sap/data”

Once in the sap folder, the code needs to be downloaded into a folder called “SAP” 
which is automatically done when the files are cloned from ‘GitHub’

“sudo git clone https://github.com/deseram07/SAP.git”

