# rccarnew_pkg
An architecture to control a RC car with ROS.

## Hardware requirements
- NodeMCU ESP8266-12E
- USB Type-A to Micro-B Cable
- L298b - motor driver
- Micro USB cable, 9V battery, bread boards.

## Software Dependencies
- ROS-noetic installed(Ubuntu 20.04) 
    - For installation of ROS-noetic refer to this wiki ros official page 
    http://wiki.ros.org/noetic/Installation/Ubuntu
- Arduino IDE & esp8266 libraries 
    - For downloading Arduino IDE and congiguring with the esp-12e board libraries you can visit this page
    https://www.embedded-robotics.com/programming-esp8266/
    - 
- xacro installed
    - Install using
    ``` 
    sudo apt install ros-noetic-xacro
    ```

## NodeMCU 1.0(ESP-12E Module)
### PINOUT
![alt text](https://www.embedded-robotics.com/wp-content/uploads/2021/05/NodeMCU-ESP8266-v1.0-Pinout-1024x538.png)


