import sys
if "emulated" in sys.argv or "EMULATED" in sys.argv :
	import GPIOEmulator as GPIO
else :
	import RPi.GPIO as GPIO
import time

class Bargraph:
	def __init__(self) :
		currentLevel = 0
		GPIO.setmode(GPIO.BCM)
		for pin in range(1,11):
			GPIO.setup(pin, GPIO.OUT)
		self.setLevel(0)
	
	def setLevel(self, level):
		for pin in range(1, 11):
			GPIO.output(pin, pin<=level)
		self.currentLevel = level

	def stepToLevel(self, level, stepTime):
		while self.currentLevel != level:
			time.sleep(stepTime)
			step = 1
			if self.currentLevel > level:
				step = -1
			self.setLevel(self.currentLevel + step)		

	def moveToLevel(self, level, overTime):
		steps = abs(self.currentLevel - level)
		if steps>0:
			self.stepToLevel(level, overTime/steps)
	
	def close(self):
		GPIO.cleanup()