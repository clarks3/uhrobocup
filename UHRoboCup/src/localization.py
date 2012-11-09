import math
import time
import camera
import config

motionProxy = config.load_proxy("ALMotion")
redballtracker = config.load_proxy("ALRedBallTracker")

def get_nao_location():
    naoID = "goalie"
    (naoX, naoY, naoZ) = motionProxy.getRobotPosition(False)
    return (naoX, naoY, naoZ, naoID)

def get_location():
    # Set stiffnes ON
    config.stiffness_on()

    #Make sure top camera is active
    camera.top_camera()

    # Start looking for red ball to track.
    redballtracker.stopTracker()
    redballtracker.startTracker()
    redballtracker.setWholeBodyOn(True)
    print "Tracking red ball"

    #Store initial red ball positon to variable
    initialredballposition = redballtracker.getPosition()
    print "Initial Position: ", initialredballposition
    cameras = 0 #Top camera
    count = 0
    counter = 0 #Used for Redballposition
    times = 0
    headpitchangle = 1.433
    while redballtracker.isActive(): # runs while loop as long as redballtracker is active
        while redballtracker.getPosition() == initialredballposition:  # Ball lost.
            if redballtracker.isNewData() == False and count == 0: # Ball still lost.true if a new Red Ball was detected since the last getPosition().
                print "Looking for red ball"
                camera.top_camera()
                motionProxy.setAngles(['HeadYaw', 'HeadPitch'], [-0.5, headpitchangle], 0.07)
                time.sleep(3)
                count = 1
                cameras = 0 # top camera
                times += 1
            elif redballtracker.isNewData() == False and count == 1:
                camera.bottom_camera()
                motionProxy.setAngles(['HeadYaw', 'HeadPitch'], [0.5, headpitchangle], 0.07)
                time.sleep(3)
                count = 0
                cameras = 1 # bottom camera
                times += 1
            # the next if condition is to look up slightly if he can't find the ball and then when it looks up 3 times
            # it decides turns left and starts all over again.
            if times > 1:
                number = float(times)
                if number % 2 == 1:
                    if headpitchangle < 0:
                        headpitchangle = 1.433
                        walk.ultimatewalkto(0, 0, 2)
                    elif headpitchangle > .5:
                        headpitchangle = .2
                    else:
                        headpitchangle = headpitchangle - 0.2
                    print headpitchangle
                else:
                    pass
        # Ball found.
        # Store found red ball positon to variable.
        #foundredballposition and foundredballposition 2 are to make sure there are no
        #random jumps so the robot doesn't randomly pick a different thing to go to.
        if counter == 0:
            foundredballposition2 = redballtracker.getPosition()
        foundredballposition = foundredballposition2
        foundredballposition2 = redballtracker.getPosition()
        print "Found red ball position: ", foundredballposition2
        redballtracker.stopTracker()
        return (foundredballposition[0], foundredballposition[1])
