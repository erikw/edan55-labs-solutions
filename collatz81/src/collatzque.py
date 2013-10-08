import queue
import heapq

class CollatzQue(queue.PriorityQueue):
    def __init__(self, *kargs, **kwargs):
        super(queue.PriorityQueue, self).__init__(*kargs, **kwargs)

    def peekLast(self):
        return self.queue[-1]

    def popLast(self):
        self.queue.pop(-1)
        heapq.heapify(self.queue)



