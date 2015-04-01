#!/usr/bin/env python

from Maestor import maestor


def theRobot():
    robot = maestor()
    bendDown(robot)
    doTheRobot(robot)
    standUp(robot)

def bendDown(robot):
    robot.setProperties("RFZ LFZ", "position position", "-.52 -.52")
    robot.waitForJoint("RFZ")
    robot.waitForJoint("LFZ")

def waitForJoints(robot):
    robot.waitForJoint("RSR")
    robot.waitForJoint("RSY")
    robot.waitForJoint("REP")

def armUp(robot):
    robot.setProperty("NKY", "position", -.65)
    robot.setProperties("RSY RSR", "position position", "1.57 -1.35")

def swingArm(robot):
    robot.setProperty("REP", "position", -1.7)
    robot.waitForJoint("REP")
    robot.setProperty("REP", "position", 0)
    robot.waitForJoint("REP")

def armDown(robot):
    robot.setProperties("RSY RSR NKY", "position position position", "0 0 0")


def doTheRobot(robot):
    armUp(robot)
    waitForJoints(robot)

    for i in range(0, 2):
        swingArm(robot)

    armDown(robot)
    waitForJoints(robot)

def standUp(robot):
    robot.setProperties("RFZ LFZ", "position position", "-.56 -.56")
    robot.waitForJoint("RFZ")
    robot.waitForJoint("LFZ")

def getDanceList():
    danceList = []
    #add all of the key parts of the dance. Including the wait for joints
    danceList.append(armUp)
    danceList.append(waitForJoints)
    danceList.append(swingArm)
    danceList.append(swingArm)
    danceList.append(swingArm)
    danceList.append(armDown)
    danceList.append(waitForJoints)

    return danceList

def theRobotRobot(robot):
    bendDown(robot)
    doTheRobot(robot)
    standUp(robot)


if __name__ == '__main__':
    theRobot()
