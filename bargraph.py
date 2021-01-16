import sys
if "emulated" in sys.argv or "EMULATED" in sys.argv :
	import GPIOEmulator as GPIO
else :
	import RPi.GPIO as GPIO
import time
import math

currentLevel = 0
	
def setLevel(level):
	global currentLevel
	for pin in range(1, 11):
		GPIO.output(pin, pin<=level)
	currentLevel = level

def stepToLevel(level, stepTime):
	while currentLevel != level:
		time.sleep(stepTime)
		step = 1
		if currentLevel > level:
			step = -1
		setLevel(currentLevel + step)		

def moveToLevel(level, overTime):
	global currentLevel
	steps = abs(currentLevel - level)
	if steps>0:
		stepToLevel(level, overTime/steps)

GPIO.setmode(GPIO.BCM)
for pin in range(1,11):
	GPIO.setup(pin, GPIO.OUT)

setLevel(0)

target = 0
while target >= 0:
    moveToLevel(target, 0.5)
    target = int(input("Level:"))

GPIO.cleanup()