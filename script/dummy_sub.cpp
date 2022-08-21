#include "ros/ros.h"
#include "std_msgs/Int32.h"
#include <iostream>

void number_callback(const std_msgs::Int32::ConstPtr& msg){
    if(msg->data==1)
    ROS_INFO("%d\n", msg->data);
    else 
    ROS_INFO("00\n");
}

int main(int argc, char **argv){
    ros::init(argc, argv,"receiver");
    ros::NodeHandle node1_obj;
    ros::Subscriber dummy_receiver= node1_obj.subscribe("/sample_signal", 200, number_callback);
    ros::spin();
    return 0;
}