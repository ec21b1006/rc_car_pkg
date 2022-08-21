#include <ESP8266WiFi.h>
#include <WiFiClient.h>
#include <ESP8266WebServer.h>
#include <ros.h>
#include <std_msgs/Int32.h>

#define DEBUG 1

//Set credentials to connect to the Wifi network 
//Change if required
const char *ssid = "sibi";
const char *password = "12345678";

IPAddress server(192, 168, 151, 113); // Set the rosserial socket ROSCORE SERVER IP address

const uint16_t serverPort = 11411; // Set the rosserial socket server port

// connect to ROS server as as a client
void setupWiFi()
{
  Serial.print("Connecting to ");
  Serial.println(ssid);
  WiFi.begin(ssid, password);

  Serial.println("");
  Serial.println("WiFi connected");
  Serial.println("IP address: ");
  Serial.println(WiFi.localIP());
}

ros::NodeHandle nh;
std_msgs::Int32 msg;

ros::Publisher pub("/sample_signal", &msg); //Publish a sample topic to check the connection, proof of concept

void setup()
{
  if (DEBUG)
    Serial.begin(115200);
  setupWiFi();
  delay(2000);

  nh.getHardware()->setConnection(server, serverPort);
  nh.initNode();
  nh.advertise(pub);
}

void loop()
{
  if (nh.connected())
  {
    Serial.println("Connected");
  }
  msg.data = 1;
  pub.publish(&msg);
  //Publish message 
  nh.spinOnce();
  delay(200);
}
