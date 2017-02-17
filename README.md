## Overview: Motion Detection

This project focuses mainly on detecting motion of an object when it enters in the AOE of the camera used. It keeps on detecting the motion for as long as the object stays within the camera/webcams effect. It has 4 different version of frames which captures the objects motion for preciseness and accuracy. It clocks in the time & date of when the object entered or exited the frame in a .xls file.

## Installing the library/ prerequisites

- numpy --> import numpy
- pandas --> import pandas

- cv2 (OpenCV) -->
 
 OpenCV was added lately in the online Python package repository so first make sure you have the latest version of pip by executing:
 
 pip install -- upgrade pip
 
 Then install OpenCV:
 pip install opencv-python 
 
 And then you can import opencv in Python as:
 import cv2 


## Running the tests
Once you have completed the entire project, you can run it in a terminal like this:

`python mdetect.py`

Keep running it and try to enter and exit the frame or use object to do so. See for the time & date of entry/exit in the saved .xls file.
