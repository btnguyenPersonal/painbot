import time
from gpiozero import Motor, PWMOutputDevice

class Vehicle:
    def __init__(self):
        self.left_motor = Motor(forward=17, backward=22)
        self.left_pwm = PWMOutputDevice(18)
        self.left_pwm.value = 0.5
        self.right_motor = Motor(forward=23, backward=24)
        self.right_pwm = PWMOutputDevice(25)
        self.right_pwm.value = 0.5

    def stop(self):
        rpi_vehicle.left_motor.stop()
        rpi_vehicle.right_motor.stop()

    def forward(self):
        rpi_vehicle.left_motor.forward()
        rpi_vehicle.right_motor.forward()

    def backward(self):
        rpi_vehicle.left_motor.backward()
        rpi_vehicle.right_motor.backward()

    def turn_left(self):
        rpi_vehicle.left_motor.backward()
        rpi_vehicle.right_motor.forward()

    def turn_right(self):
        rpi_vehicle.left_motor.forward()
        rpi_vehicle.right_motor.backward()

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
