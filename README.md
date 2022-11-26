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
