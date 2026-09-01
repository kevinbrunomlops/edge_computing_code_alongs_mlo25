import time
from machine import Pin, PWM

MAX_U16 = 2**16

time.sleep(0.1)

led = {
    "red": Pin(15, Pin.OUT),
    "green": Pin(14, Pin.OUT)
}

button = Pin(13, Pin.IN, Pin.PULL_UP)

button_state = {
    "pressed": False,
    "last_interrupt_time": 0
}

buzzer = PWM(Pin(12))
buzzer.freq(1000)
buzzer.duty_u16(0)

def button_callback(pin):
    current_time = time.ticks_ms()
    if (current_time - button_state["last_interrupt_time"]) > 200:
        button_state["pressed"] = False if button_state["pressed"] else True
        button_state["last_interrupt_time"] = current_time

button.irq(trigger = Pin.IRQ_FALLING, handler = button_callback)

while True:
    if button_state["pressed"]:
        led["green"].value(1)
        led["red"].value(0)
        
        for i in range(10):
            buzzer.duty_u16(int(MAX_U16/100)*i)
            time.sleep(.1)
            buzzer.duty_u16(int(MAX_U16/100)*(100-i))
            time.sleep(.3)
        time.sleep(.5)
    button_state["pressed"] = False
    buzzer.duty_u16(0)
    led["green"].value(0)
    led["red"].value(1)
    time.sleep(3)