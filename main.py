#beatMan
from machine import Pin ,PWM
from utime import sleep
servo0 = PWM(Pin(0))
servo1 = PWM(Pin(1))
servo0.freq(50)
servo1.freq(50)

ini_0 , ini_1 = 5000 , 5500
make_0 , make_1 = 4000 , 3500

servo0.duty_u16(ini_0)
servo1.duty_u16(ini_1)

def dian(tampo):
    servo0.duty_u16(make_0)
    sleep(0.1)
    servo0.duty_u16(ini_0)
    sleep(tampo*0.15+0.05)

def ko(tampo):
    servo1.duty_u16(make_1)
    sleep(0.1)
    servo1.duty_u16(ini_1)
    sleep(tampo*0.15+0.05)

#start
while True:    
    for i in range(2):
        for j in range(8):
            ko(1)
        for j in range(16):
            ko(0)

    dian(0)

    for j in range(8):
        ko(3)
        
    for i in range(4):
        for j in range(2):
            ko(1)
        for j in range(4):
            ko(0)
    for i in range(2):
        ko(1)
        ko(1)
        dian(3)
    for i in range(16):
        ko(0)
    for k in range(3):
        dian(3)
