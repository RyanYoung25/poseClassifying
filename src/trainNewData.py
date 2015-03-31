#!/usr/bin/env python
from kinect import Kinect
from jsonConverter import jsonMaker
from datetime import datetime
import time
import sys


def main():
    dances = ["ChickenDance", "Disco", "WalkLikeAnEgy", "YMCA"]
    print "Please Enter a unique number for this participant.\n if the number already exisits data will be over written."
    personNum = raw_input('> ')
    user = 1

    for dance in dances:
        filename = dance + str(personNum) + ".log"
        print "The next dance that will be recored is: " + str(dance)
        print "The data will be stored in the file: " + str(filename)
        print "The user being recorded is: " + str(user)
        print "Press enter when ready to record..."
        raw_input("")

        filePath = "../data/" + filename
        f = open(filePath, "w")

        if len(sys.argv) == 2:
            user = int(sys.argv[1])
        print "recording"
        time.sleep(1)
        user1 = Kinect(user=user)
        for i in range(0, 1000):
            val =  user1.get_posture()
            if val != None:
                tup = (str(datetime.now().time()),  val)
                newLine = jsonMaker(tup)
                print i
                f.write(str(newLine) + "\n")
            time.sleep(.03) 
        f.close() 

if __name__ == '__main__':
    main()
