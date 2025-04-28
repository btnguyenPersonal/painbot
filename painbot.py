import time
from gpiozero import Motor, PWMOutputDevice

class Vehicle:
    __init__(self):
        self.left_motor = Motor(forward=17, backward=22)
        self.left_pwm = PWMOutputDevice(18)
        self.left_pwm.value = 0.5

rpi_vehicle = Vehicle()

def main():
    i = 0
    while True:
        print("forward " + str(i))
        i += 1
        rpi_vehicle.left_motor.forward()
        time.sleep(0.5)
        rpi_vehicle.left_motor.stop()
        time.sleep(0.5)

main()