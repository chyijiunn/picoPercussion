from machine import Pin ,I2C , PWM ,Timer
from ssd1306 import SSD1306_I2C
from time import sleep
import _thread , sys

oled = SSD1306_I2C(128, 64, I2C(0,sda=Pin(20), scl=Pin(21), freq=40000))
buttonU = Pin(0, Pin.IN, Pin.PULL_UP)
buttonD = Pin(1, Pin.IN, Pin.PULL_UP)
buttonL = Pin(2, Pin.IN, Pin.PULL_UP)
buttonR = Pin(3, Pin.IN, Pin.PULL_UP)
buttonA = Pin(14, Pin.IN, Pin.PULL_UP)
buttonB = Pin(15, Pin.IN, Pin.PULL_UP)
buzzer = PWM(Pin(13))
buzzer.freq(500)
minute = 0.5

def counter(tim):
    buzzer.duty_u16(1000)
    sleep(0.1)
    buzzer.duty_u16(0)

tim = Timer(-1)
tim.init(period=int(60*1000*minute), mode=Timer.PERIODIC, callback=counter)