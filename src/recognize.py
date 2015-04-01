#!/usr/bin/env python

import sys
import os
from kinect import Kinect
from AngleCalculator import generateAngles
from useClassifier import *
import time
from datetime import datetime
from jsonConverter import jsonMaker
from multiprocessing import Process, Manager
#Include the dances
from dances.Maestor import maestor
from dances.ChickenDance import chickenDanceRobot
from dances.disco import stayAliveRobot
from dances.walkLikeAnEgyptian import walkLikeAnEgyptianRobot
from dances.YMCA import doTheYMCARobot


loadClassifier()

#Get the current gesture happening and classify it. Then print the result
def classifyCurrentGesture(d):
    user = Kinect(user=1)
    goodString = None
    while goodString is None:
        val =  user.get_posture()
        if val is not None:
            tup = (str(datetime.now().time()),  val)
            goodString = jsonMaker(tup)
        time.sleep(.25) 

    angles = generateAngles(goodString)
    classList = classifySample(angles)
    theDance = ""
    if len(classList) != 0:
        theDance = classList[0]
    #d[0] = 1
    f = open(".tmp.val", "w")
    f.write(theDance)
    f.close()


def respondDance(res):
    #Switch on the result of the dance pose classificaiton
    #and perform an appropriate dance in response.
    robot = maestor()
    f = open(".tmp.val", "r")
    line = f.readline()
    result = line
    f.close()
    print result
    if result == "Disco":
        stayAliveRobot(robot)
    elif result == "ChickenDance":
        chickenDanceRobot(robot)
    elif result == "WalkLikeAnEgyptian":
        walkLikeAnEgyptianRobot(robot)
    elif result == "YMCA":
        doTheYMCARobot(robot)
    else:
        print "No dance recognized"




def main():
    keepGoing = True
    manager = Manager()
    d = manager.dict()
    d['a'] = ""
    while keepGoing:
        print "Enter q to quit"
        print "Enter anything else to recognize and dance"
        result = raw_input('> ')
        if result is "q":
            keepGoing = False
            continue
        p1 = Process(target=classifyCurrentGesture, args=(d,))
        p2 = Process(target=respondDance, args=(d,))
        p1.start()
        p1.join()
        print d
        p2.start()
        p2.join()

if __name__ == '__main__':
    main()
    os.remove(".tmp.val")
