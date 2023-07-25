from machine import Timer,Pin,PWM
import time
buzzer = PWM(Pin(13))
buzzer.freq(500)

def buzz(tim):
    buzzer.duty_u16(65500)
    time.sleep(0.01)
    buzzer.duty_u16(0)

tim = Timer(-1)
tim.init(period=1000, mode=Timer.PERIODIC, callback=buzz)