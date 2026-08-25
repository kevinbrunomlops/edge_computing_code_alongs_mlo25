import json 
import rp2
import network 
import time 

rp2.country("SE")

with open("wifi_credentials.json") as file:
    credentials = json.load(file)


def connect_wifi(waiting_time = 10):
    # pico becomes a client to connect to wifi 
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True) #powers on radio WIFI on pico W/2W
    wlan.connect(credentials.get("SSID"), credentials.get("PASSWORD"))

    while waiting_time > 0:
        if wlan.isconnected():
            print("You are connected")
            break 

        waiting_time -= 1
        print("Try to connect to wifi, wait a little bit")
        time.sleep(1)

    return wlan.isconnected()

print(credentials)