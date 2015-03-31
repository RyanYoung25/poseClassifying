#!/usr/bin/env python

from kinect import Kinect
from datetime import datetime
import sys
import time
import json

def jsonMaker(tup):
    dict = {
            "Time" : tup[0],
            "Joints" : [                   
                {
                    "name": joint[0],
                    "pos" : {
                        "x" : joint[1][0],
                        "y" : joint[1][1],
                        "z" : joint[1][2]
                    },
                    "rot" : {
                        "x" : joint[2][0],
                        "y" : joint[2][1],
                        "z" : joint[2][2],
                        "w" : joint[2][3]
                    }
                } for joint in tup[1]
            ]
    }

    return json.dumps(dict)


def main():
    f = open("PositionsChkn.log", "w")

    user = 1
    if len(sys.argv) == 2:
        user = int(sys.argv[1])
    print "sleeping"
    time.sleep(7)
    user1 = Kinect(user=user)
    for i in range(0, 1000):
        val =  user1.get_posture()
        if val != None:
            tup = (str(datetime.now().time()),  val)
            newLine = jsonMaker(tup)
            print newLine
            f.write(str(newLine) + "\n")
        time.sleep(.03) 
    f.close() 
    


if __name__ == '__main__':
    main()
