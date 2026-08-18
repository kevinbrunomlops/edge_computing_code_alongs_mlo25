from time import sleep

from machine import Pin

sleep(1)

led_internal = Pin("LED", 1)

led_internal.value(1)

led_internal.value(0)
