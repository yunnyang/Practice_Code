#295. Find Median from Data Stream
import bisect

class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stream = list()

    def addNum(self, num: int) -> None:
        bisect.insort(self.stream,num)
    def findMedian(self) -> float:
        k = len(self.stream)
        return (self.stream[int(k / 2)] + self.stream[~int(k / 2)]) / 2.


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()