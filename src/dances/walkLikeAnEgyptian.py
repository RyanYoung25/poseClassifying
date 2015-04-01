#!/usr/bin/env python
from Maestor import maestor

def wait_for_joint(robot):
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

def one_way_S(robot):
    robot.setProperty("RSP", "position", -0.001)
    robot.setProperty("RSR", "position", -1.278)
    robot.setProperty("RSY", "position", -1.511)
    robot.setProperty("LSP", "position", 0.004)
    robot.setProperty("LSR", "position", 1.146)
    robot.setProperty("LSY", "position", -1.508)
    robot.setProperty("REP", "position", -1.21)
    robot.setProperty("LEP", "position", -1.723)
    robot.setProperty("RWP", "position", 1.319)
    robot.setProperty("LWP", "position", 1.138)
    robot.setProperty("RWY", "position", 0.082)
    robot.setProperty("LWY", "position", 0.03)
    robot.setProperty("NKY", "position", -.75)

def one_way_extended(robot):
    robot.setProperty("RSP", "position", -0.001)
    robot.setProperty("RSR", "position", -1.278)
    robot.setProperty("RSY", "position", -1.488)
    robot.setProperty("LSP", "position", 0.003)
    robot.setProperty("LSR", "position", 1.146)
    robot.setProperty("LSY", "position", -1.454)
    robot.setProperty("REP", "position", -0.437)
    robot.setProperty("LEP", "position", -0.71)
    robot.setProperty("RWP", "position", 0.727)
    robot.setProperty("LWP", "position", 0.902)
    robot.setProperty("RWY", "position", 0.033)
    robot.setProperty("LWY", "position", 0.07)

def other_way_S(robot):
    robot.setProperty("RSP", "position", -0.0)
    robot.setProperty("RSR", "position", -1.278)
    robot.setProperty("RSY", "position", 1.523)
    robot.setProperty("LSP", "position", 0.002)
    robot.setProperty("LSR", "position", 1.146)
    robot.setProperty("LSY", "position", 1.654)
    robot.setProperty("REP", "position", -1.511)
    robot.setProperty("LEP", "position", -1.577)
    robot.setProperty("RWP", "position", 1.209)
    robot.setProperty("LWP", "position", 1.326)
    robot.setProperty("RWY", "position", 0.025)
    robot.setProperty("LWY", "position", 0.15)
    robot.setProperty("NKY", "position", .75)
    
def other_way_extended(robot):
    robot.setProperty("RSP", "position", 0.001)
    robot.setProperty("RSR", "position", -1.278)
    robot.setProperty("RSY", "position", 1.52)
    robot.setProperty("LSP", "position", 0.002)
    robot.setProperty("LSR", "position", 1.146)
    robot.setProperty("LSY", "position", 1.653)
    robot.setProperty("REP", "position", -0.694)
    robot.setProperty("LEP", "position", -0.873)
    robot.setProperty("RWP", "position", 0.841)
    robot.setProperty("LWP", "position", 0.84)
    robot.setProperty("RWY", "position", -0.002)
    robot.setProperty("LWY", "position", 0.17)

def upper_body_home(robot):
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
    robot.setProperty("NKY", "position", 0)

def crouch(robot):
    robot.setProperties("RFZ LFZ", "position position", "-.52 -.52")
    robot.waitForJoint("RFZ")
    robot.waitForJoint("LFZ")

def stand(robot):
    robot.setProperties("RFZ LFZ", "position position", "-.56 -.56")
    robot.waitForJoint("RFZ")
    robot.waitForJoint("LFZ")

def walkLikeAnEgyptian():
    robot = maestor()
    crouch(robot)
    for i in xrange(0, 3):
        
        for i in xrange(0, 2): 
            one_way_S(robot)
            wait_for_joint(robot)
            one_way_extended(robot)
            wait_for_joint(robot)

        for i in xrange(0, 2):    
            other_way_S(robot)
            wait_for_joint(robot)
            other_way_extended(robot)
            wait_for_joint(robot)
    
    upper_body_home(robot)
    wait_for_joint(robot)
    stand(robot)

def walkLikeAnEgyptianRobot(robot):
    crouch(robot)
    for i in xrange(0, 3):
        
        for i in xrange(0, 2): 
            one_way_S(robot)
            wait_for_joint(robot)
            one_way_extended(robot)
            wait_for_joint(robot)

        for i in xrange(0, 2):    
            other_way_S(robot)
            wait_for_joint(robot)
            other_way_extended(robot)
            wait_for_joint(robot)
    
    upper_body_home(robot)
    wait_for_joint(robot)
    stand(robot)

def getDanceList():
    danceList = []
    #add all of the key parts of the dance. Including the wait for joints
    for i in xrange(0, 2):
        danceList.append(one_way_S)
        danceList.append(wait_for_joint)
        danceList.append(one_way_extended)
        danceList.append(wait_for_joint)

    for i in xrange(0, 2):
        danceList.append(other_way_S)
        danceList.append(wait_for_joint)
        danceList.append(other_way_extended)
        danceList.append(wait_for_joint)


    return danceList

if __name__ == '__main__':
    walkLikeAnEgyptian()
