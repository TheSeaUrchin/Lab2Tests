# Library imports
from vex import *
import math

# Brain should be defined by default
brain=Brain()


# Robot configuration code
left_motor = Motor(Ports.PORT1, GearSetting.RATIO_18_1, True)
right_motor = Motor(Ports.PORT2, GearSetting.RATIO_18_1, False)
arm_motor = Motor(Ports.PORT5, GearSetting.RATIO_18_1, False)
dtrain = DriveTrain(left_motor, right_motor)
ultraSensor = Sonar(brain.three_wire_port.c)
imu = Inertial(Ports.PORT19)
LEMON = Signature(1, 1327, 3121, 2224, -3971, -3523, -3747, 2.5, 0)
LIME = Signature(2, -6019, -5317, -5668, -4145, -3443, -3794, 2.5, 0)
ORNG = Signature(3, 5901, 8115, 7008, -2619, -2227, -2423, 2.5, 0)
GRAPEFRUIT = Signature(4, 3821, 6393, 5107, 1099, 1471, 1285, 2.5, 0)
Vision15 = Vision(Ports.PORT15,25 , LEMON, LIME, ORNG, GRAPEFRUIT)


ROBOT_IDLE = 0
ROBOT_SEARCHING = 1
## start in the idle state
state = ROBOT_IDLE
def handleButtonPress():
    global state
    if(state == ROBOT_IDLE):
        print("IDLE -> SEARCHING")
        arm_motor.reset_position()
        state = ROBOT_SEARCHING
        right_motor.spin(FORWARD,defaultSpeed)
        left_motor.spin(FORWARD,-defaultSpeed)
    
#left_motor.spin(FORWARD, 30)
#right_motor.spin(FORWARD, -30)
    else:
        print(' -> IDLE')
        left_motor.stop()
        right_motor.stop()
    
button5 = Bumper(brain.three_wire_port.a)
button5.pressed(handleButtonPress)
def handleObjects(objects):
    obj = Vision15.largest_object()
    cx = obj.centerX
    cy = obj.centerY
    #print(cx, cy)
    centering(cx)
    print(distanceCalc(obj.height))
    if(distanceCalc(obj.height)<7):
        left_motor.stop()
        right_motor.stop()
        grabFruit()
        wait(5000)
    

defaultSpeed = 150
def centering(x):
    global defaultSpeed
    center = 160-4
    error = center - x
    effort = error
    right_motor.set_velocity(defaultSpeed-effort)
    left_motor.set_velocity(defaultSpeed+effort)

def distanceCalc(pxH):
    h = 3
    theta = 1.1
    totalScreen = 6600/7
    Pct = pxH/totalScreen

    screenSize=h/Pct

    d = 0.5 * screenSize/math.tan(theta)
    d +=0.5
    return d

def grabFruit():
    global arm_motor
    arm_motor.spin_to_position(-920,velocity = 50,wait=True)
    wait(1000)
    arm_motor.spin_to_position(-800,velocity = 50,wait=True)


    

while True:
    objects = Vision15.take_snapshot(ORNG)
    if objects and state == ROBOT_SEARCHING:
        handleObjects(objects)

    sleep(20)
