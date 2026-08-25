from wifi import connect_wifi
from machine import Pin

status_led = Pin(15,1)


if connect_wifi():
    status_led.value(1)