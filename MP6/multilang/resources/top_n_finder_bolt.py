import heapq
from collections import Counter

import storm


class TopNFinderBolt(storm.BasicBolt):
    # Initialize this instance
    def initialize(self, conf, context):
        self._conf = conf
        self._context = context

        storm.logInfo("Counter bolt instance starting...")
        self._topN = dict()
        self._len = len(self._topN)

        # TODO:
        # Task: set N
        pass
        # End

        # Hint: Add necessary instance variables and classes if needed

    def process(self, tup):
        '''
        TODO:
        Task: keep track of the top N words
        Hint: implement efficient algorithm so that it won't be shutdown before task finished
              the algorithm we used when we developed the auto-grader is maintaining a N size min-heap
        '''
        word = tup.values[0]
        count = float(tup.values[1])
        storm.logInfo("Emitting laida lasan %s:%s" % (word, count))

        self._topN[word]=count
        

        while len(self._topN) > 10:
            key_to_delete = min(self._topN.keys(), key=lambda k: self._topN[k])
            del self._topN[key_to_delete]
        
        mytopN = "top-N"
        values= ""
        counter = 0
        for i in self._topN.keys():
            if counter == 0:
                values = values + i
            else:
                values = values + "," + i
         
        storm.logInfo("betichod") 
        storm.logInfo("Emitting %s:%s" % (mytopN, values))
        storm.emit([mytopN,values])

        pass
        # End


# Start the bolt when it's invoked
TopNFinderBolt().run()
