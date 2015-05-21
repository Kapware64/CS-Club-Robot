
import RPi.GPIO as GPIO  
import time


pinLeft = 10
pinRight = 8


GPIO.setmode(GPIO.BOARD)

GPIO.setup(pinLeft, GPIO.OUT) 
GPIO.setup(pinRight, GPIO.OUT)



def turnOnLeft():
    GPIO.output(pinLeft, 1)
 
def turnOffLeft():
    GPIO.output(pinLeft, 0)


def turnOnRight():
    GPIO.output(pinRight, 1)

def turnOffRight():
    GPIO.output(pinRight, 0)


def turnOnBoth():
    turnOnRight()
    turnOnLeft()


def turnOffBoth():
    turnOffLeft()
    turnOffRight()


def turnAround():
        turnOffLeft()
        turnOnRight()
        time.sleep(random.uniform(a,b))
        turnOffRight()
        time.sleep(random.uniform(a,b))

turnOnLeft()
time.sleep(5)
turnOffLeft()
time.sleep(1)
turnOnBoth()
time.sleep(5)
turnOffBoth()

GPIO.cleanup()
