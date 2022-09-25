class MyCircularQueue(object):

    def __init__(self, k):
        """
        :type k: int
        """
        self.size = k
        self.queue = []
        self.count = 0

    def enQueue(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if self.count < self.size:
            self.queue.append(value)
            self.count += 1
            return True
        else:
            return False
    

    def deQueue(self):
        """
        :rtype: bool
        """
        if self.count > 0:
            self.queue.pop(0)
            self.count -= 1
            return True
        else:
            return False

    def Front(self):
        """
        :rtype: int
        """
        try:
            return self.queue[0]
        except:
            return -1

    def Rear(self):
        """
        :rtype: int
        """
        try:
            return self.queue[-1]
        except:
            return -1

    def isEmpty(self):
        """
        :rtype: bool
        """
        return self.count == 0

    def isFull(self):
        """
        :rtype: bool
        """
        return self.count == self.size


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()