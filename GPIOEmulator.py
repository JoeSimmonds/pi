from time import time as timeNow
import curses


class Emulator :
    def __init__(self) :
        self.BOARD = "BOARD"
        self.BCM = "BCM"
        self.OUT = "output"
        self.IN = "input"
        self.mode = self.BOARD
        self.physicalToGPIO = {3  : 2, 5  : 3, 7  : 4, 8  : 14, 10 : 15, 11 : 17, 12 : 18,
        13 : 27, 15 : 22, 16 : 23, 18 : 24, 19 : 10, 21 : 9, 22 : 25, 23 : 11, 24 : 8,
        26 : 7, 27 : 0, 28 : 1, 29 : 5, 31 : 6, 32 : 12, 33 : 13, 35 : 19, 36 : 16, 37 : 26, 38 : 20, 40 : 21}
        self.GPIOtoPhysical = {gpio:phys for phys, gpio in self.physicalToGPIO.iteritems()}
        self.startTime = timeNow()

    def log(self, msg) :
        print("T+" + str(timeNow() - self.startTime) + " | " + msg)

    def pinDescription(self, pin) :
        if self.mode == BOARD :
            physicalPin = pin
            gpioPin = self.physicalToGPIO.get(pin)
        else :
            gpioPin = pin
            physicalPin = self.GPIOtoPhysical.get(pin)
        return "pin " + str(physicalPin) + "(GPIO" + str(gpioPin) + ")"

em = Emulator()

BOARD = em.BOARD
BCM = em.BCM
OUT = em.OUT
IN = em.IN

def setmode(mode) :
    em.mode = mode
    em.log("mode set to " + mode)

def setup(pin, direction) :
    em.log(em.pinDescription(pin) + " set as " + direction)

class PWMInfo:
    def __init__(self, pin, freq):
        self.pin = pin
        self.freq = freq

    def start(self, dutyCycle) :
        em.log(em.pinDescription(self.pin) + " PWM started with duty cycle " + str(dutyCycle) + "%")
    
    def ChangeDutyCycle(self, dutyCycle) :
        em.log("PWM duty cycle for " + em.pinDescription(self.pin) + " changed to " + str(dutyCycle) + "%")

    def stop(self) :
        emulatorUtils.log("PWM stopped for " + em.pinDescription(self.pin))
    

def PWM(pin, freq) :
    em.log(em.pinDescription(pin) + " initialised for PWM with frequency " + str(freq) +"Hz")
    return PWMInfo(pin, freq)

def cleanup() :
    em.log("GPIO cleaned up and shutdown")

def output(pin, isHigh) :
    if (isHigh) :
        state = "high"
    else :
        state = "low"
    em.log(em.pinDescription(pin) + " set to " + state)