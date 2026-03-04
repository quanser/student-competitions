import time

import urllib.request
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
trafficLightIPs = str("192.168.2.20")

#Define the length of red, yellow, green
redTime = str(3)
yellowTime = str(3)
greenTime = str(3)

#Turn the adjacent traffic lights on at the same time
print(sendreq("http://" + trafficLightIPs + ":5000/timed/" + redTime + "/" + yellowTime + "/" + greenTime))
