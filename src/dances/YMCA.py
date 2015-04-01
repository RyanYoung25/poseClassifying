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

def theY(robot):
    robot.setProperty("RSP", "position", 0.0)
    robot.setProperty("RSR", "position", -1.98)
    robot.setProperty("RSY", "position", -1.55)
    robot.setProperty("LSP", "position", 0.0)
    robot.setProperty("LSR", "position", 1.93)
    robot.setProperty("LSY", "position", 1.64)
    robot.setProperty("REP", "position", -0.22)
    robot.setProperty("LEP", "position", -0.32)
    robot.setProperty("RWP", "position", 0.0)
    robot.setProperty("LWP", "position", 0.0)
    robot.setProperty("RWY", "position", -1.42)
    robot.setProperty("LWY", "position", 1.54)

def theM(robot):
    robot.setProperty("RSP", "position", 0.0)
    robot.setProperty("RSR", "position", -1.98)
    robot.setProperty("RSY", "position", 1.576)
    robot.setProperty("LSP", "position", 0.0)
    robot.setProperty("LSR", "position", 1.93)
    robot.setProperty("LSY", "position", -1.45)
    robot.setProperty("REP", "position", -1.95)
    robot.setProperty("LEP", "position", -2.09)
    robot.setProperty("RWP", "position", 0.0)
    robot.setProperty("LWP", "position", 0.0)
    robot.setProperty("RWY", "position", -1.42)
    robot.setProperty("LWY", "position", 1.54)

def theC(robot):
    robot.setProperty("RSP", "position", 0.0)
    robot.setProperty("RSR", "position", -1.98)
    robot.setProperty("RSY", "position", -1.42)
    robot.setProperty("LSP", "position", 0.0)
    robot.setProperty("LSR", "position", 0.0)
    robot.setProperty("LSY", "position", 1.62)
    robot.setProperty("REP", "position", -1.18)
    robot.setProperty("LEP", "position", -0.82)
    robot.setProperty("RWP", "position", 0.0)
    robot.setProperty("LWP", "position", 0.0)
    robot.setProperty("RWY", "position", -1.42)
    robot.setProperty("LWY", "position", 1.54)

def theA(robot):
    robot.setProperty("RSP", "position", 0.0)
    robot.setProperty("RSR", "position", -1.98)
    robot.setProperty("RSY", "position", -1.42)
    robot.setProperty("LSP", "position", 0.0)
    robot.setProperty("LSR", "position", 1.98)
    robot.setProperty("LSY", "position", 1.62)
    robot.setProperty("REP", "position", -1.35)
    robot.setProperty("LEP", "position", -1.35)
    robot.setProperty("RWP", "position", 0.0)
    robot.setProperty("LWP", "position", 0.0)
    robot.setProperty("RWY", "position", -1.42)
    robot.setProperty("LWY", "position", 1.54)

def upperBodyHome(robot):
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

def crouch(robot):
    robot.setProperties("RFZ LFZ", "position position", "-.52 -.52")
    robot.waitForJoint("RFZ")
    robot.waitForJoint("LFZ")

def stand(robot):
    robot.setProperties("RFZ LFZ", "position position", "-.56 -.56")
    robot.waitForJoint("RFZ")
    robot.waitForJoint("LFZ")


def doTheYMCA():
    robot = maestor()
    crouch(robot)
    for i in xrange(0,3):   #for(int i=0; i < 3; i ++) 
        theY(robot)
        waitForJoints(robot)
        theM(robot)
        waitForJoints(robot)
        theC(robot)
        waitForJoints(robot)
        theA(robot)
        waitForJoints(robot)
        upperBodyHome(robot)
        waitForJoints(robot)
    stand(robot)

def doTheYMCARobot(robot):
    crouch(robot)
    for i in xrange(0,3):   #for(int i=0; i < 3; i ++) 
        theY(robot)
        waitForJoints(robot)
        theM(robot)
        waitForJoints(robot)
        theC(robot)
        waitForJoints(robot)
        theA(robot)
        waitForJoints(robot)
        upperBodyHome(robot)
        waitForJoints(robot)
    stand(robot)

def getDanceList():
    danceList = []
    #add all of the key parts of the dance. Including the wait for joints
    danceList.append(theY)
    danceList.append(waitForJoints)
    danceList.append(theM)
    danceList.append(waitForJoints)
    danceList.append(theC)
    danceList.append(waitForJoints)
    danceList.append(theA)
    danceList.append(waitForJoints)
    danceList.append(upperBodyHome)
    danceList.append(waitForJoints)

    return danceList

if __name__ == '__main__':
    doTheYMCA() 
