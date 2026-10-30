class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minHeap = nums
        self.k = k
        heapq.heapify(self.minHeap)  #use the heapq.heapify to convery the list into a heap
        while len(self.minHeap) > k: #if theres more elements than k just remove the smallest ones
            heapq.heappop(self.minHeap)
    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val) #push
        if len(self.minHeap) > self.k: #only pop elements if adding makes it larger than k elements
            heapq.heappop(self.minHeap)
        return self.minHeap[0] #return the first element in a minheap
        
