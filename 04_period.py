from machine import Pin ,PWM ,Timer
from utime import sleep
servo = PWM(Pin(0))
servo.freq(50)

def motor(tim):
    servo.duty_u16(5000)
    sleep(0.1)
    servo.duty_u16(3000)

tim = Timer(-1)
tim.init(period=1000, mode=Timer.PERIODIC, callback=motor)