from machine import Pin, PWM
import time

MAX_U16 = 2**16

led_ref = Pin(14, Pin.OUT)
led_ref.value(1)

led_pwd = PWM(Pin(15))
led_pwd.freq(1000)
led_pwd.duty_u16(int(MAX_U16/3))
while True:
    for i in range(100):
        led_pwd.duty_u16(int(MAX_U16/100)*i)
        time.sleep(.01)
    for i in range(100):
        led_pwd.duty_u16(int(MAX_U16/100)*(100-i))
        time.sleep(.01)