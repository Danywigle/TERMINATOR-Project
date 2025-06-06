# This is a library for the Terminator Robot
# It contains functions to control the robot's movements.
# It is designed to be used with the Terminator Robot's hardware (4 Motors and 1 Ultrasonic Sensor).
# The code is written in Python and uses the GPIO library to control the motors.
# The code is designed to be run on a Raspberry Pi.

# Import the necessary libraries
from gpiozero import PWMOutputDevice, DistanceSensor
from time import sleep

# Define the GPIO pins for the motors
motor_left_forward = PWMOutputDevice(17)
motor_left_backward = PWMOutputDevice(27)
motor_right_forward = PWMOutputDevice(3)
motor_right_backward = PWMOutputDevice(2)
motor_backleft_forward = PWMOutputDevice(10)
motor_backleft_backward = PWMOutputDevice(9)
motor_backright_forward = PWMOutputDevice(19)
motor_backright_backward = PWMOutputDevice(26)
# Define the GPIO pin for the ultrasonic sensor
sonar = DistanceSensor(echo=4, trigger=22, max_distance=1.0)

def forward_slow():
    """
    Move the robot forward slowly (0.4).
    """
    motor_left_forward.value = 0.4  # Set the motor to move forward at half speed
    motor_left_backward.value = 0  # Stop the backward motor
    motor_right_forward.value = 0.4  # Set the motor to move forward at half speed
    motor_right_backward.value = 0  # Stop the backward motor
    motor_backleft_forward.value = 0.4  # Set the motor to move forward at half speed
    motor_backleft_backward.value = 0  # Stop the backward motor
    motor_backright_forward.value = 0.4  # Set the motor to move forward at half speed
    motor_backright_backward.value = 0  # Stop the backward motor
def forward_mid():
    """
    Move the robot forward at medium speed (0.7).
    """
    motor_left_forward.value = 0.7  # Set the motor to move forward at medium speed
    motor_left_backward.value = 0  # Stop the backward motor
    motor_right_forward.value = 0.7  # Set the motor to move forward at medium speed
    motor_right_backward.value = 0  # Stop the backward motor
    motor_backleft_forward.value = 0.7  # Set the motor to move forward at medium speed
    motor_backleft_backward.value = 0  # Stop the backward motor
    motor_backright_forward.value = 0.7  # Set the motor to move forward at medium speed
    motor_backright_backward.value = 0  # Stop the backward motor
def forward_fast():
    """
    Move the robot forward at full speed (1).
    """
    motor_left_forward.value = 1.0  # Set the motor to move forward at full speed
    motor_left_backward.value = 0  # Stop the backward motor
    motor_right_forward.value = 1.0  # Set the motor to move forward at full speed
    motor_right_backward.value = 0  # Stop the backward motor
    motor_backleft_forward.value = 1.0  # Set the motor to move forward at full speed
    motor_backleft_backward.value = 0  # Stop the backward motor
    motor_backright_forward.value = 1.0  # Set the motor to move forward at full speed
    motor_backright_backward.value = 0  # Stop the backward motor
def backward_slow():
    """
    Move the robot backward slowly (0.4).
    """
    motor_left_backward.value = 0.4  # Set the motor to move backward at half speed
    motor_left_forward.value = 0  # Stop the forward motor
    motor_right_backward.value = 0.4  # Set the motor to move backward at half speed
    motor_right_forward.value = 0  # Stop the forward motor
    motor_backleft_backward.value = 0.4  # Set the motor to move backward at half speed
    motor_backleft_forward.value = 0  # Stop the forward motor
    motor_backright_backward.value = 0.4  # Set the motor to move backward at half speed
    motor_backright_forward.value = 0  # Stop the forward motor
def backward_fast():
    """
    Move the robot backward at full speed (0.7).
    """
    motor_left_backward.value = 0.7 # Set the motor to move backward at full speed
    motor_left_forward.value = 0  # Stop the forward motor
    motor_right_backward.value = 0.7  # Set the motor to move backward at full speed
    motor_right_forward.value = 0  # Stop the forward motor
    motor_backleft_backward.value = 0.7  # Set the motor to move backward at full speed
    motor_backleft_forward.value = 0  # Stop the forward motor
    motor_backright_backward.value = 0.7  # Set the motor to move backward at full speed
    motor_backright_forward.value = 0  # Stop the forward motor
def stop():
    """
    Stop the robot.
    """
    motor_left_forward.value = 0  # Stop the forward motor
    motor_left_backward.value = 0  # Stop the backward motor
    motor_right_forward.value = 0  # Stop the forward motor
    motor_right_backward.value = 0  # Stop the backward motor
    motor_backleft_forward.value = 0  # Stop the forward motor
    motor_backleft_backward.value = 0  # Stop the backward motor
    motor_backright_forward.value = 0  # Stop the forward motor
    motor_backright_backward.value = 0  # Stop the backward motor
def direct_left():
    """
    Rotate the robot to the left (F-B).
    """
    motor_left_forward.value = 0  # Stop the forward motor
    motor_left_backward.value = 0.4  # Set the motor to move backward at half speed
    motor_right_forward.value = 0.4  # Set the motor to move forward at half speed
    motor_right_backward.value = 0  # Stop the backward motor
    motor_backleft_forward.value = 0  # Stop the forward motor
    motor_backleft_backward.value = 0.4  # Set the motor to move backward at half speed
    motor_backright_forward.value = 0.4  # Set the motor to move forward at half speed
    motor_backright_backward.value = 0  # Stop the backward motor
def direct_right():
    """
    Rotate the robot to the right (B-F).
    """
    motor_left_forward.value = 0.4  # Set the motor to move forward at half speed
    motor_left_backward.value = 0  # Stop the backward motor
    motor_right_forward.value = 0  # Stop the forward motor
    motor_right_backward.value = 0.4  # Set the motor to move backward at half speed
    motor_backleft_forward.value = 0.4  # Set the motor to move forward at half speed
    motor_backleft_backward.value = 0  # Stop the backward motor
    motor_backright_forward.value = 0  # Stop the forward motor
    motor_backright_backward.value = 0.4  # Set the motor to move backward at half speed
def turn_left():
    """
    Rotate the robot to the left (0.6-0.4) (This needs more testing).
    """
    motor_left_forward.value = 0.6  # Set the motor to move forward at half speed
    motor_left_backward.value = 0  # Stop the backward motor
    motor_right_forward.value = 0.4  # Set the motor to move forward at half speed
    motor_right_backward.value = 0  # Stop the backward motor
    motor_backleft_forward.value = 0.6  # Set the motor to move forward at half speed
    motor_backleft_backward.value = 0  # Stop the backward motor
    motor_backright_forward.value = 0.4  # Set the motor to move forward at half speed
    motor_backright_backward.value = 0  # Stop the backward motor
def turn_right():
    """
    Rotate the robot to the right (0.4-0.6) (This needs more testing).
    """
    motor_left_forward.value = 0.4  # Set the motor to move forward at half speed
    motor_left_backward.value = 0  # Stop the backward motor
    motor_right_forward.value = 0.6  # Set the motor to move forward at half speed
    motor_right_backward.value = 0  # Stop the backward motor
    motor_backleft_forward.value = 0.4  # Set the motor to move forward at half speed
    motor_backleft_backward.value = 0  # Stop the backward motor
    motor_backright_forward.value = 0.6  # Set the motor to move forward at half speed
    motor_backright_backward.value = 0  # Stop the backward motor
def distance_front():
    """
    Get the distance from the ultrasonic sensor.
    """
    return sonar.distance  # Return the distance from the ultrasonic sensor
