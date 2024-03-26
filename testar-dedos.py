from pyfirmata import Arduino,SERVO
import time

board = Arduino('COM3')

pin1 = 10
pin2 = 9
pin3 = 8
pin4 = 7
pin5 = 6

board.digital[pin1].mode = SERVO
board.digital[pin2].mode = SERVO
board.digital[pin3].mode = SERVO
board.digital[pin4].mode = SERVO
board.digital[pin5].mode = SERVO

def rotateServo(pino,angle):
    board.digital[pino].write(angle)
    time.sleep(0.015)


rotateServo(pin1,0)
rotateServo(pin2,0)
rotateServo(pin3,0)
rotateServo(pin4,0)
rotateServo(pin5,0)
time.sleep(1)

rotateServo(pin1,150)
time.sleep(1)
rotateServo(pin1,0)
time.sleep(1)

rotateServo(pin2,130)
time.sleep(1)
rotateServo(pin2,0)
time.sleep(1)

rotateServo(pin3,130)
time.sleep(1)
rotateServo(pin3,0)
time.sleep(1)

rotateServo(pin4,130)
time.sleep(1)
rotateServo(pin4,0)
time.sleep(1)

rotateServo(pin5,130)
time.sleep(1)
rotateServo(pin5,0)
time.sleep(2)