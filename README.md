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

Setting up the deamon:
The deamon file can be found in the admin folder

Move the file sap into /etc/init.d directory
Make the file executable

To start the program
  /etc/init.d/sap start
To stop the program
	/etc/init.d/sap stop

To restart the software 60s after it dies, you need to add the 
program onto crontab. To do this
	sudo crontab-e

Add the line
	***** /etc/init.d/sap start

To start the program automatically on startup. You need to use update-rc.d
	sudo update-rc.d -f sap defaults

And if you ever want to delete it
	sudo update-rc.d -f sap remove

