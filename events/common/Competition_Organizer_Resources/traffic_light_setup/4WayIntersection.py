# imports

from pal.products.traffic_light import TrafficLight
import time
# -- -- -- -- -- -- -- -- -- -- -- 
light1_ip = '192.168.2.20'
light2_ip = '192.168.2.21'
light3_ip = '192.168.2.22'
light4_ip = '192.168.2.23'
# -- -- -- -- -- -- -- -- -- -- --

# Initialize a Traffic Light with its corresponding IP

# initialize 7 traffic light instances in qlabs
trafficLight1 = TrafficLight(light1_ip)
time.sleep(1)
trafficLight2 = TrafficLight(light2_ip)
time.sleep(1)
trafficLight3 = TrafficLight(light3_ip)
time.sleep(1)
trafficLight4 = TrafficLight(light4_ip)
time.sleep(1)

# Check the status of the lights
status1 = trafficLight1.status()
print("Traffic Light 1 Status is: " + status1)

status2 = trafficLight2.status()
print("Traffic Light 2 Status is: " + status2)

# status3 = trafficLight3.status()
# print("Traffic Light 3 Status is: " + status3)

status4 = trafficLight4.status()
print("Traffic Light 4 Status is: " + status4)

print('check all lights are in a 0 state')
time.sleep(3)

#intersection setup

#       +y              #
# --------------------- #
#        1
#   2         3
#        4
# --------------------- #

# Go into loop

intersection1Flag = 0

try:

    while(True):

        #intersection 1
        if intersection1Flag == 0:
            trafficLight1.green()
            trafficLight4.green()
            trafficLight2.red()
            trafficLight3.red()
        
        if intersection1Flag == 1:
            trafficLight1.yellow()
            trafficLight4.yellow()
            trafficLight2.red()
            trafficLight3.red()

        if intersection1Flag == 2:
            trafficLight1.red()
            trafficLight4.red()
            trafficLight2.green()
            trafficLight3.green()

        if intersection1Flag == 3:
            trafficLight1.red()
            trafficLight4.red()
            trafficLight2.yellow()
            trafficLight3.yellow()

        #if the intersection does not have yellows, hold for longer
        if intersection1Flag%2 == 0:
            time.sleep(2)
        
        intersection1Flag = (intersection1Flag + 1)%4

        time.sleep(3)
    
finally:
   # Turn off the traffic light with shutting down
    input('Waiting to terminate lights press enter')
    turnOff = trafficLight1.off()
    trafficLight2.off()
    trafficLight3.off()
    trafficLight4.off()
    print(turnOff) 

