#!/usr/bin/env python
from Maestor import maestor

def waitForJoints(robot):
    robot.waitForJoint("RSP")
    robot.waitForJoint("RSR")
    robot.waitForJoint("RSY")
    robot.waitForJoint("LSP")
    robot.waitForJoint("LSR")
    robot.waitForJoint("LSY")
    robot.waitForJoint("REP")
    robot.waitForJoint("LEP")
    robot.waitForJoint("RWP")
    robot.waitForJoint("LWP")
    robot.waitForJoint("RWY")
    robot.waitForJoint("LWY")
    robot.waitForJoint("WST")

def armUp(robot):
    robot.setProperty("WST", "velocity", 0.3)
    robot.setProperty("RSP", "position", -0.287)
    robot.setProperty("RSR", "position", -2.215)
    robot.setProperty("RSY", "position", 0.239)
    robot.setProperty("LSP", "position", 0)
    robot.setProperty("LSR", "position", 0)
    robot.setProperty("LSY", "position", 0)
    robot.setProperty("REP", "position", 0)
    robot.setProperty("LEP", "position", 0)
    robot.setProperty("RWP", "position", 0.101)
    robot.setProperty("LWP", "position", 0)
    robot.setProperty("RWY", "position", 0.082)
    robot.setProperty("LWY", "position", 0)
    robot.setProperty("WST", "position", -.3)
    robot.setProperty("WST", "velocity", 1)

def armDown(robot):
    robot.setProperty("WST", "velocity", 0.3)
    robot.setProperty("RSP", "position", -0.287)
    robot.setProperty("RSR", "position", -0.054)
    robot.setProperty("RSY", "position", 0.958)
    robot.setProperty("LSP", "position", 0)
    robot.setProperty("LSR", "position", 0)
    robot.setProperty("LSY", "position", 0)
    robot.setProperty("REP", "position", -0.852)
    robot.setProperty("LEP", "position", 0)
    robot.setProperty("RWP", "position", -0.229)
    robot.setProperty("LWP", "position", 0)
    robot.setProperty("RWY", "position", 0.368)
    robot.setProperty("LWY", "position", 0)
    robot.setProperty("WST", "position", .3)
    robot.setProperty("WST", "velocity", 1)

def upperToZero(robot):
    robot.setProperty("RSP", "position", 0)
    robot.setProperty("RSR", "position", 0)
    robot.setProperty("RSY", "position", 0)
    robot.setProperty("LSP", "position", 0)
    robot.setProperty("LSR", "position", 0)
    robot.setProperty("LSY", "position", 0)
    robot.setProperty("REP", "position", 0)
    robot.setProperty("LEP", "position", 0)
    robot.setProperty("RWP", "position", 0)
    robot.setProperty("LWP", "position", 0)
    robot.setProperty("RWY", "position", 0)
    robot.setProperty("LWY", "position", 0)
    robot.setProperty("WST", "position", 0)

def crouch(robot):
    robot.setProperties("RFZ LFZ", "position position", "-.52 -.52")
    robot.waitForJoint("RFZ")
    robot.waitForJoint("LFZ")

def stand(robot):
    robot.setProperties("RFZ LFZ", "position position", "-.56 -.56")
    robot.waitForJoint("RFZ")
    robot.waitForJoint("LFZ")

def stayAlive():
    robot = maestor()
    crouch(robot)
    robot.setProperty("WST", "velocity", 0.3)
    for i in xrange(0, 5):
        armUp(robot)
        waitForJoints(robot)
        armDown(robot)
        waitForJoints(robot)
    upperToZero(robot)
    robot.setProperty("WST", "velocity", 1)
    stand(robot)

def getDanceList():
    danceList = []
    #add all of the key parts of the dance. Including the wait for joints
    danceList.append(armUp)
    danceList.append(waitForJoints)
    danceList.append(armDown)
    danceList.append(waitForJoints)

    return danceList

def stayAliveRobot(robot):
    crouch(robot)
    robot.setProperty("WST", "velocity", 0.3)
    for i in xrange(0, 5):
        armUp(robot)
        waitForJoints(robot)
        armDown(robot)
        waitForJoints(robot)
    upperToZero(robot)
    robot.setProperty("WST", "velocity", 1)
    stand(robot)


if __name__ == '__main__':
    stayAlive()
