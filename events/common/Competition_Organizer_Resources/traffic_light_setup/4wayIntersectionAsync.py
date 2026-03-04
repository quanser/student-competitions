import time
import math
import struct

from quanser.communications import Stream
import urllib.request, sys
from urllib.error import HTTPError, URLError
from socket import timeout

#Send the formatted request
def sendreq(url):
    #Format the HTTP get request with a timeout of 1s to account for async tasks that will not return

    response = "Call complete!"
    try:
        response = urllib.request.urlopen(url, timeout=1).read().decode('utf-8')
    #If the URL is not correct
    except (HTTPError, URLError) as error:
        response = "Error endpoint not found at " + url
    #If the request was not expected to return the call it complete, otherwise flag a timeout
    except timeout:
        if url.find("timed") == -1:
            response = "Call timed out"
        else:
            response = "Async call complete"

    return response

#Define the traffic lights in use
trafficLightIPs = ["192.168.2.20", "192.168.2.21", "192.168.2.22", "192.168.2.23"]

#Define the length of red, yellow, green
redTime = str(11)
yellowTime = str(3)
greenTime = str(8)

#Turn the adjacent traffic lights on at the same time
print(sendreq("http://" + trafficLightIPs[1] + ":5000/timed/" + redTime + "/" + yellowTime + "/" + greenTime))
print(sendreq("http://" + trafficLightIPs[3] + ":5000/timed/" + redTime + "/" + yellowTime + "/" + greenTime))

#Wait for first 2 traffic lights to finish their red light duration before changing the next 2 traffic lights on
time.wait(11)

#Turn the other adjacent traffic lights on at the same time
print(sendreq("http://" + trafficLightIPs[2] + ":5000/timed/" + redTime + "/" + yellowTime + "/" + greenTime))
print(sendreq("http://" + trafficLightIPs[4] + ":5000/timed/" + redTime + "/" + yellowTime + "/" + greenTime))