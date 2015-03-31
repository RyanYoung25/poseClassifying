#!/usr/bin/env python

from kinect import Kinect
from AngleCalculator import generateAngles
from useClassifier import *
import time
from datetime import datetime
from jsonConverter import jsonMaker

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
        time.sleep(.03) 

    angles = generateAngles(goodString)
    result = classifySample(angles)
    print result

def main():
    while True:
        classifyCurrentGesture()

if __name__ == '__main__':
    time.sleep(10)
    main()
