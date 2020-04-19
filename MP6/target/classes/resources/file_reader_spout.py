# import os
# from os.path import join
from time import sleep

# from streamparse import Spout
import storm


class FileReaderSpout(storm.Spout):

    def initialize(self, conf, context):
        self._conf = conf
        self._context = context
        self._complete = False

        storm.logInfo("Spout instance starting...")
        #self._myreaderfile = self._conf[input.file] 
        self._myreadfilepointer = open("/mp6/solution/CloudComputing/data.txt")
        #storm.logInfo("%s",self._myreaderfile)
        storm.logInfo("see this fucked up thing")

        # TODO:
        # Task: Initialize the file reader
        pass
        # End

    def nextTuple(self):
        # TODO:
        # Task 1: read the next line and emit a tuple for it
        line = self._myreadfilepointer.readline()
        if line:
            storm.logInfo("%s" %line)
            storm.emit([line.lower()])
        else:
            storm.emit("End of file")
            sleep(1)

        # Task 2: don't forget to sleep for 1 second when the file is entirely read to prevent a busy-loop

            
        pass
        # End


# Start the spout when it's invoked
FileReaderSpout().run()
