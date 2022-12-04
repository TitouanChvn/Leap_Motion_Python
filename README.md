# Leap_Motion_Python
Python Application for a __Leap Motion Controller__


I recently aquiered a Leap Motion Controller and I will be coding for it.
It is a device that allows us to track one's hands with precision and analyse their movments.

Leap Motion has an API for Python, Java, Javascript, C++,C#. it also has modules to interact with Unreal and Unity.[API Documentation] (https://developer-archive.leapmotion.com/documentation/python/devguide/Project_Setup.html)

The Python API requires that we use python 2.7 as latest versions are not supported.


-------


In this example we will first see how to gather data for each hand on each frame taken by the controller.

The data we are looking for are hand number, hand position, finger number, finger position, normal vector to the hand and more.

The function to access this informations are described in the Leap API documentation

-----

## Main functionalities
Executing the batch file will give the user a choice of different options : 
* print data captured by the controler on each frame
* display real time hands position 
* move the mouse on the screen by moving your hand where you want the mouse to be (absolute position)
* move the mouse from a certain amount by swiping your hand in a direction (relative position)
* ultimately allow user to fully control the cursor remotely (movements, clicks, draging, scrolling etc..)
* and create an imaginary keyboard that allow you to type without touching a keyboard.

-----
## Why the batch file ? (and the communication file)
Different parts of the program requieres different versions of python.

The Leap API requieres that we use python 2.7 but to select the options i used Pyinquierer which doesnt work with 2.7. The batch file allow me to execute each script with it's own interpreter. It is therefore necessary to pass information from one program to another witch is done by the communication.txt file.
* the first line of the file represents the options chosen by the user
