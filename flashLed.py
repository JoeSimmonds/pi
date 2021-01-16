import GPIOEmulator as GPIO
import time
import math
import curses

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)

rateHz = 0.5

p = GPIO.PWM(11, 50)
p.start(0)
rate = rateHz * 360
startTime = time.time()
while time.time() <= startTime + 12:
    timeNow = time.time()
    brightness = (math.sin(math.radians((timeNow*rate)%361))/2 + 0.5)
    p.ChangeDutyCycle(brightness * 100)
    sleepTime = max(10 - rateHz, 0.0)/500
    time.sleep(sleepTime)

p.stop()
GPIO.cleanup()

