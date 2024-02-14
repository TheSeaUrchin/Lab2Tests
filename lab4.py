# ---------------------------------------------------------------------------- #
#                                                                              #
# 	Module:       main.py                                                      #
# 	Author:       josh                                                         #
# 	Created:      2/10/2024, 7:20:54 PM                                        #
# 	Description:  V5 project                                                   #
#                                                                              #
# ---------------------------------------------------------------------------- #

# Library imports
from vex import *

# Brain should be defined by default
brain = Brain()
controller = Controller(PRIMARY);

isStopped = True

left_motor = Motor(Ports.PORT10, True)
right_motor = Motor(Ports.PORT1)
arm_motor = Motor(Ports.PORT6)
dump_motor = Motor(Ports.PORT5)
string_motor = Motor(Ports.PORT9)

dump_motor.set_max_torque(25, PERCENT)
string_motor.set_max_torque(25, PERCENT)
arm_motor.set_max_torque(25, PERCENT)

button = Bumper(brain.three_wire_port.a)

# uses tank drive configuration to update motors based on controller input
def update_drivetrain():
    left_motor.set_velocity(controller.axis3.position(), PERCENT)
    right_motor.set_velocity(controller.axis2.position(), PERCENT)
    left_motor.spin(FORWARD)
    right_motor.spin(FORWARD)

def grab():
    string_motor.spin(FORWARD, 100, PERCENT)
def release():
    string_motor.spin(REVERSE,100, PERCENT)
def dumpOut():
    dump_motor.spin(FORWARD,100)
def dumpIn():
    dump_motor.spin(REVERSE,100)
def armUp():
    arm_motor.spin(FORWARD,50)
def armDown():
    arm_motor.spin(REVERSE,50)

def kill():
    left_motor.stop(BRAKE)
    right_motor.stop(BRAKE)
    arm_motor.stop(BRAKE)
    dump_motor.stop(BRAKE)
    string_motor.stop(BRAKE)



# sets up button events for tightening and loosening string on grabbing mechanism
controller.buttonUp.pressed(grab)
controller.buttonUp.released(lambda : string_motor.stop(BrakeType.HOLD))
controller.buttonDown.pressed(release)
controller.buttonDown.released(lambda : string_motor.stop(BrakeType.HOLD))

# sets up button events for moving dumping mechanism
controller.buttonLeft.pressed(dumpOut)
controller.buttonLeft.released(lambda : dump_motor.stop(BrakeType.HOLD))
controller.buttonRight.pressed(dumpIn)
controller.buttonRight.released(lambda : dump_motor.stop(BrakeType.HOLD))

# sets up button events for moving arm up and down
controller.buttonX.pressed(armUp)
controller.buttonX.released(lambda : arm_motor.stop(BrakeType.HOLD))
controller.buttonB.pressed(armDown)
controller.buttonB.released(lambda : arm_motor.stop(BrakeType.HOLD))

# kill switch
button.pressed(kill)

while True:
    update_drivetrain()

    wait(10)

    # controls spool that tightens string on grabbing mechanism using A/B buttons
    # if controller.buttonA:
    #     string_motor.spin(FORWARD, 15, RPM)
    # elif controller.buttonB:
    #     string_motor.spin(REVERSE, 15, RPM)
    # else:
    #     string_motor.stop()

    # # moves arm up and down using X/Y buttons
    # if controller.button:
    #     arm_motor.spin(FORWARD, 15, RPM)
    # elif controller.buttonY:
    #     arm_motor.spin(REVERSE, 15, RPM)
    # else:
    #     arm_motor.stop()

    # # moves dumping mechanism back and forth using L1/R1 buttons
    # if controller.buttonL1:
    #     dump_motor.spin(FORWARD, 15, RPM)
    # elif controller.buttonR1:
    #     dump_motor.spin(REVERSE, 15, RPM)
    # else:
    #     dump_motor.stop()

    
        
