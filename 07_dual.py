from machine import Pin ,PWM
from utime import sleep
import _thread
servoPINx = PWM(Pin(0))
servoPINx.freq(50)
servoPINy = PWM(Pin(1))
servoPINy.freq(50)

def motorA():
    while 1:
        servoPINx.duty_u16(4000)
        sleep(0.4)
        servoPINx.duty_u16(5000)
        sleep(0.4)

def motorB():
    servoPINy.duty_u16(8900)
    sleep(0.05)
    servoPINy.duty_u16(7000)
    sleep(0.5)
    
_thread.start_new_thread(motorA, ())
while 1:
    motorB()