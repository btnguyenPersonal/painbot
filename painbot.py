import curses
import time
from gpiozero import Motor, PWMOutputDevice

class Vehicle:
    def __init__(self):
        self.left_motor = Motor(forward=17, backward=22)
        self.left_pwm = PWMOutputDevice(18)
        self.left_pwm.value = 1
        self.right_motor = Motor(forward=23, backward=24)
        self.right_pwm = PWMOutputDevice(25)
        self.right_pwm.value = 1

    def stop(self):
        print("stop")
        rpi_vehicle.left_motor.stop()
        rpi_vehicle.right_motor.stop()

    def forward(self):
        print("forward")
        rpi_vehicle.left_motor.forward()
        rpi_vehicle.right_motor.forward()

    def backward(self):
        print("backward")
        rpi_vehicle.left_motor.backward()
        rpi_vehicle.right_motor.backward()

    def turn_left(self):
        print("turn_left")
        rpi_vehicle.right_motor.forward()

    def turn_right(self):
        print("turn_right")
        rpi_vehicle.left_motor.forward()

rpi_vehicle = Vehicle()

def main(stdscr):
    stdscr.nodelay(1)
    while True:
        c = stdscr.getch()
        stdscr.addstr("\n\n")
        stdscr.refresh()
        stdscr.move(0, 0)
        if c != -1:
            if c == 119:
                rpi_vehicle.forward()
            elif c == 115:
                rpi_vehicle.backward()
            elif c == 97:
                rpi_vehicle.turn_left()
            elif c == 100:
                rpi_vehicle.turn_right()
        else:
            rpi_vehicle.stop()
        time.sleep(0.5)

if __name__ == "__main__":
    curses.wrapper(main)
