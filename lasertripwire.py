from machine import ADC, Pin
from utime import sleep_ms
ldr = ADC(26)
led = Pin(15, Pin.OUT)

def flick():
    if led.value() == 0:
        led.value(1)
    else:
        led.value(0)
        
prev = ldr.read_u16()
while True:
    ll = ldr.read_u16()
    diff = ll-prev
    if diff > 10000 or diff < -10000:
        flick()
    sleep_ms(333)
    prev = ll