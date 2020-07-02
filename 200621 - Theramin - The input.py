# Write your code here :-)
from gpiozero import DistanceSensor
from time import sleep

from pythonosc import osc_message_builder
from pythonosc import udp_client

sensor1 = DistanceSensor(echo=17, trigger=4)
sensor2 = DistanceSensor(echo=26, trigger=19)

sender = udp_client.SimpleUDPClient('127.0.0.1', 4559)

while True:
    print (sensor1.distance)
    print (sensor2.distance)
    pitch = round(sensor1.distance * 100 +30)
    sender.send_message('/play_this', pitch)
    sleep(0.06)

#Okay so both sensors work, providing a distance reading. Good. However, the results all display in the one stream.
#I think 2 streams are required... unless I get the recieved to read every other line of the stream... thoughts?
