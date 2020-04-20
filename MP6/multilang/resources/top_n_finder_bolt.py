import heapq
from collections import Counter

import storm


class WordCountTuple:

    def __init__(self, word, count):
        self.word = word
        self.count = count

    def __cmp__(self, inword):
        return self.count > inword.count


class TopNFinderBolt(storm.BasicBolt):

    def initialize(self, conf, context):
        self._conf = conf
        self._context = context
        storm.logInfo("Counter bolt instance starting...")
        self._top_words = Counter()
        self._N = 10
        self._top_N_map = {}
        self._top_N_heap = []

    def process(self, tup):
        '''
        TODO:
        Task: keep track of the top N words
        Hint: implement efficient algorithm so that it won't be shutdown before task finished
        the algorithm we used when we developed the auto-grader is maintaining a N size min-heap
        '''
        word = tup.values[0]
        count = int(tup.values[1])

        new_word_count = WordCountTuple(word, count)

        if word in self._top_N_map:
            if count > self._top_N_map[word].count:
                self._top_N_map[word].count = count
                heapq.heapify(self._top_N_heap)

         #adding new elements if the element size is less than 10        
        elif len(self._top_N_heap) < self._N:
            self._top_N_map[word] = new_word_count
            heapq.heappush(self._top_N_heap, new_word_count)

         #find smallest word and replace it with new word    
        else:
            smallest_word_count = self._top_N_heap[0]

            if count > smallest_word_count.count:
                del(self._top_N_map[smallest_word_count.word])
                self._top_N_map[word] = new_word_count
                heapq.heapreplace(self._top_N_heap, new_word_count)
                storm.logInfo("Add word: %s, count: %d" % (word, count))

        storm.emit(["top-N", self.report()])
        pass
    


    def report(self):
        words = [word_count.word for word_count in self._top_N_heap]

        return ", ".join(words)


# Start the bolt when it's invoked
TopNFinderBolt().run()

