#include <ESP8266WiFi.h>
#include <WiFiClient.h>
#include <ESP8266WebServer.h>
#include <ros.h>
#include <std_msgs/Int32.h>

#define DEBUG 1

const char* ssid = "sibi";
const char* password = "12345678";
IPAddress server(192,168,151,113);      // Set the rosserial socket ROSCORE SERVER IP address
  //Set the rosserial socket server port

//const char *ssid = "espbrooo";
//const char *password = "sexysundar";
//IPAddress server;
const uint16_t serverPort = 11411;  
void setupWiFi() {                    // connect to ROS server as as a client
    Serial.print("Connecting to ");
    Serial.println(ssid);
    WiFi.begin(ssid, password);
//  while (WiFi.status() != WL_CONNECTED) {
//    delay(500);
//  }
    Serial.println("");
    Serial.println("WiFi connected");
    Serial.println("IP address: ");
    Serial.println(WiFi.localIP());
}

ros::NodeHandle nh;
std_msgs::Int32 msg;

ros::Publisher pub("/sex", &msg);

void setup() {
  if(DEBUG) Serial.begin(115200);
  setupWiFi();
  delay(2000);
//  WiFi.softAP(ssid, password);
//
//  IPAddress myIP = WiFi.softAPIP();
//  Serial.print("AP IP address: ");
//  Serial.println(myIP);
//
//   //server = &(wifi_softap_get_station_info())->ip;
//   server = (192,168,4,2);
//
//   delay(10000);
  nh.getHardware()->setConnection(server, serverPort);
  nh.initNode();
  nh.advertise(pub);
   
 

}

void loop() {
  if (nh.connected()) {
    Serial.println("Connected");
   
  }
  msg.data=1;
  pub.publish(&msg);
  nh.spinOnce();
  delay(200);
}
