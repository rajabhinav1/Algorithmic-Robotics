

import RPi.GPIO as GPIO
import time

# Define the GPIO pins for motor control
motor1_pin1 = 18
motor1_pin2 = 23
motor2_pin1 = 24
motor2_pin2 = 25

# Set GPIO mode and pin numbering
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Set up GPIO pins as output
GPIO.setup(motor1_pin1, GPIO.OUT)
GPIO.setup(motor1_pin2, GPIO.OUT)
GPIO.setup(motor2_pin1, GPIO.OUT)
GPIO.setup(motor2_pin2, GPIO.OUT)
c. Define functions for robot movements:


# Define functions for robot movements
def move_forward():
    GPIO.output(motor1_pin1, GPIO.HIGH)
    GPIO.output(motor1_pin2, GPIO.LOW)
    GPIO.output(motor2_pin1, GPIO.HIGH)
    GPIO.output(motor2_pin2, GPIO.LOW)

def move_backward():
    GPIO.output(motor1_pin1, GPIO.LOW)
    GPIO.output(motor1_pin2, GPIO.HIGH)
    GPIO.output(motor2_pin1, GPIO.LOW)
    GPIO.output(motor2_pin2, GPIO.HIGH)

def stop():
    GPIO.output(motor1_pin1, GPIO.LOW)
    GPIO.output(motor1_pin2, GPIO.LOW)
    GPIO.output(motor2_pin1, GPIO.LOW)
    GPIO.output(motor2_pin2, GPIO.LOW)


//Control the robot based on user input:



while True:
    command = input("Enter command (f/b/s): ")

    if command == 'f':
        print("Moving forward...")
        move_forward()
        time.sleep(1)  # Move forward for 1 second
        stop()
    elif command == 'b':
        print("Moving backward...")
        move_backward()
        time.sleep(1)  # Move backward for 1 second
        stop()
    elif command == 's':
        print("Stopping...")
        stop()
    else:
        print("Invalid command. Please try again.")
