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
    servoPINy.duty_u16(7000)
    sleep(0.2)
    servoPINy.duty_u16(6600)
    sleep(0.2)
    servoPINy.duty_u16(7000)
    sleep(0.2)

motorB()