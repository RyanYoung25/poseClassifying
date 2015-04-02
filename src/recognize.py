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
    #Make a kinect object to listen to the skeleton data
    user = Kinect(user=1)
    goodString = None
    tries = 0
    #Try for a number of times to get good data from the kinect object.
    # If the kinect object gives good data we can make a good json string
    while goodString is None and tries < 4:
        val =  user.get_posture()
        if val is not None:
            tup = (str(datetime.now().time()),  val)
            goodString = jsonMaker(tup)
        time.sleep(.25) 
        tries += 1
    
    #If we went over the number of tries
    if goodString is None:
        return
    
    #Classify the dance based off of the angles generated from the kinect data.
    angles = generateAngles(goodString)
    classList = classifySample(angles)
    theDance = ""
    if len(classList) != 0:
        theDance = classList[0]
    #d[0] = 1
    #This is a hacky way of IPC, I know it's slow but it works for now
    safeRemove(".tmp.val")
    f = open(".tmp.val", "w")
    f.write(theDance)
    f.close()


def respondDance(res):
    #Switch on the result of the dance pose classificaiton
    #and perform an appropriate dance in response.
    robot = maestor()
    fileName = ".tmp.val"
    if not os.path.exists(fileName):
        return
    f = open(fileName, "r")
    line = f.readline()
    result = line
    f.close()
    safeRemove(fileName)
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


def safeRemove(fileName):
    try:
        os.remove(fileName)
    except OSError as e:
        pass


def main():
    keepGoing = True
    manager = Manager()
    d = manager.dict()
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
        p2.start()
        p2.join()

if __name__ == '__main__':
    main()
    safeRemove(".tmp.val")
