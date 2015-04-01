#! /usr/bin/env python
from Maestor import maestor


def crouch(robot):
    robot.setProperties("RFZ LFZ", "position position", "-.52 -.52")
    robot.waitForJoint("RFZ")
    robot.waitForJoint("LFZ")

def moveArmsUp(robot):
    robot.setProperties("RSP RSR RSY REP", "position position position position", "0 -1.27 0 -1.8")
    robot.setProperties("LSP LSR LSY LEP", "position position position position", "0 1.27 0 -1.8")
    robot.waitForJoint("RSP")
    robot.waitForJoint("RSR")
    robot.waitForJoint("RSY")
    robot.waitForJoint("REP")
    robot.waitForJoint("LSP")
    robot.waitForJoint("LSR")
    robot.waitForJoint("LSY")
    robot.waitForJoint("LEP")

def Dance(robot):
    robot.setProperties("RSR LSR", "velocity velocity", "2 2")
    for i in xrange(0, 3):
        flapUp(robot)

        flapDown(robot)

    armsMiddle(robot)
    robot.setProperties("RSR LSR", "velocity velocity", "1 1")

def flapUp(robot):
    robot.setProperty("RSR", "position", -1.85)
    robot.setProperty("LSR", "position", 1.85)
    robot.waitForJoint("RSR")
    robot.waitForJoint("LSR")

def flapDown(robot):
    robot.setProperty("RSR", "position", -.85)
    robot.setProperty("LSR", "position", .85)
    robot.waitForJoint("RSR")
    robot.waitForJoint("LSR") 

def armsMiddle(robot):
    robot.setProperty("RSR", "position", -1.27)
    robot.setProperty("LSR", "position", 1.27)
    robot.waitForJoint("RSP")
    robot.waitForJoint("LSR")

def twistAndDance(robot):
    for i in xrange(0, 3):
        twistLeft(robot)
        Dance(robot)
        twistRight(robot)
        Dance(robot)
    centerTwist(robot)

def twistLeft(robot):
    robot.setProperty("WST", "position", -.45)
    robot.waitForJoint("WST")

def twistRight(robot):
    robot.setProperty("WST", "position", .45)
    robot.waitForJoint("WST")

def centerTwist(robot):
    robot.setProperty("WST", "position", 0)
    robot.waitForJoint("WST")


def moveArmsDown(robot):
    robot.setProperties("RSP RSR RSY REP", "position position position position", "0 0 0 0")
    robot.setProperties("LSP LSR LSY LEP", "position position position position", "0 0 0 0")
    robot.waitForJoint("RSP")
    robot.waitForJoint("RSR")
    robot.waitForJoint("RSY")
    robot.waitForJoint("REP")

def stand(robot):
    robot.setProperties("RFZ LFZ", "position position", "-.56 -.56")
    robot.waitForJoint("RFZ")
    robot.waitForJoint("LFZ")

def chickenDance():
    robot = maestor()
    crouch(robot)
    moveArmsUp(robot)
    twistAndDance(robot)
    moveArmsDown(robot)
    stand(robot)

def chickenDanceRobot(robot):
    crouch(robot)
    moveArmsUp(robot)
    twistAndDance(robot)
    moveArmsDown(robot)
    stand(robot)

def getDanceList():
    danceList = []
    #add all of the key parts of the dance.    
    #arms ups
    danceList.append(moveArmsUp)
    #twist left
    danceList.append(twistLeft)
    #dance
    for i in xrange(0, 2):
        danceList.append(flapUp)
        danceList.append(flapDown)
    #twist right
    danceList.append(twistRight)
    #dance
    for i in xrange(0, 2):
        danceList.append(flapUp)
        danceList.append(flapDown)


    return danceList

if __name__ == '__main__':
    chickenDance()