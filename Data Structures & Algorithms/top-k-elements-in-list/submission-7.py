class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Step 1: build a dictionary of frequency of each number in the input
        #         Key   = Number
        #         Value = Frequency
        freq = {}
        for num in nums:
            freq[num] = 1 + freq.get(num, 0)

        # Step 2: Build a MinHeap so that we can O(1) pop the least frequent value
        #         from the top of the Heap so that we can keep size K
        minHeap = []
        for num, frequency in freq.items():
            heapq.heappush(minHeap, (frequency, num))
            if len(minHeap) > k:
                heapq.heappop(minHeap)

        # Step 3: Build result array
        res = []
        for i in range(k):
            res.append(heapq.heappop(minHeap)[1])
        return res

# Time: O(n)    -   n = size of input array, even though we did multiple loop is not double loops
# Space: O(n)   -   n = size of input array, the Heap can have all unique and multiple size
        

        