# rccarnew_pkg
An architecture to control a RC car with ROS.

## Hardware requirements
- ESP-12e module(NodeMCU 1.0)
- L298 - motor driver
- Micro USB cable, 9V battery, bread boards.

## Software Dependencies
- ROS-noetic installed(Ubuntu 20.04) 
    - For installation of ROS-noetic refer to this wiki ros official page 
    http://wiki.ros.org/noetic/Installation/Ubuntu
- Arduino IDE & esp8266 libraries 
    - For downloading Arduino IDE and congiguring with the esp12-e board you can visit this page
    https://www.embedded-robotics.com/programming-esp8266/
    - 
- xacro installed
    - Install using
    ``` 
    sudo apt install ros-noetic-xacro
    ```

    seeing the change