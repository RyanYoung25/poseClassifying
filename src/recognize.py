#!/usr/bin/env python

import Kinect
from AngleCalculator import generateAngles
from useClassifier import *

loadClassifier()

#Get the current gesture happening and classify it. Then print the result
def classifyCurrentGesture():
    user = Kinect(user=1)
    goodString = None
    while goodString is not None:
        val =  user.get_posture()
        if val != None:
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
    main()