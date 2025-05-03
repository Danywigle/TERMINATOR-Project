import terminatorlib as tlib
from gpiozero import PWMOutputDevice, DistanceSensor
from time import sleep

# while True: # Movement Test
    # Testing the robot's movement functions
    # Commenting all lines as requested
    # tlib.forward_slow()
    # print("Moving forward slowly")
    # sleep(2)
    # tlib.forward_mid()
    # print("Moving forward at medium speed")
    # sleep(2)
    # tlib.forward_fast()
    # print("Moving forward fast")
    # sleep(2)
    # tlib.backward_slow()
    # print("Moving backward slowly")
    # sleep(2)
    # tlib.backward_fast()
    # print("Moving backward fast")
    # sleep(2)
    # tlib.stop()
    # print("Stopping")
    # sleep(2)
    # tlib.direct_left()
    # print("Rotating left")
    # sleep(2)
    # tlib.direct_right()
    # print("Rotating right")
    # sleep(2)
    # tlib.turn_left()
    # print("Turning left")
    # sleep(2)
    # tlib.turn_right()
    # print("Turning right")
    # sleep(2)
while True: # Obstacle Avoidance Test
    tlib.forward_mid()
    tlib.distance_front()
    if tlib.distance_front() < 0.3:
        print("ATTENTION! Obstacle detected!")
        tlib.stop()
        sleep(0.5)
        tlib.backward_slow()
        sleep(3)
        tlib.turn_right()
        sleep(3)
        tlib.forward_mid()
    
