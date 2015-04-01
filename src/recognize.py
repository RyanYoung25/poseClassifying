#!/usr/bin/env python

import sys
from kinect import Kinect
from AngleCalculator import generateAngles
from useClassifier import *
import time
from datetime import datetime
from jsonConverter import jsonMaker
#Include the dances
from dances.Maestor import maestor
from dances.ChickenDance import chickenDanceRobot
from dances.disco import stayAliveRobot
from dances.walkLikeAnEgyptian import walkLikeAnEgyptianRobot
from dances.YMCA import doTheYMCARobot


loadClassifier()
user = Kinect(user=1)

#Get the current gesture happening and classify it. Then print the result
def classifyCurrentGesture():
    goodString = None
    while goodString is None:
        val =  user.get_posture()
        if val is not None:
            tup = (str(datetime.now().time()),  val)
            goodString = jsonMaker(tup)
        time.sleep(.25) 

    angles = generateAngles(goodString)
    result = classifySample(angles)

    return result

def respondDance(robot):
    #Switch on the result of the dance pose classificaiton
    #and perform an appropriate dance in response.
    result = classifyCurrentGesture()
    ["Disco", "ChickenDance", "WalkLikeAnEgyptian", "YMCA"]

    if result is "Disco":
        stayAliveRobot(robot)
    elif result is "ChickenDance":
        chickenDanceRobot(robot)
    elif result is "WalkLikeAnEgyptian":
        walkLikeAnEgyptianRobot(robot)
    elif result is "YMCA":
        doTheYMCARobot(robot)
    else:
        print "No dance recognized"




def main():
    keepGoing = True
    robot = maestor()
    while keepGoing:
        print "Enter q to quit"
        print "Enter anything else to recognize and dance"
        result = raw_input('> ')
        if result is "q":
            keepGoing = False
            continue
        respondDance(robot)

if __name__ == '__main__':
    main()
