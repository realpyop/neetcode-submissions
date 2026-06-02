class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 1) Find the frequency of each elements in input 
        freq = {}
        for num in nums:
            freq[num] = 1 + freq.get(num, 0)

        # 2) build a MinHeap of size K with (freq, value)
        min_heap = []
        for num in freq.keys():
            heapq.heappush(min_heap, (freq[num], num))
            if len(min_heap) > k:
                heapq.heappop(min_heap)

        # 3) build result array
        res = []
        for i in range(k):
            res.append(heapq.heappop(min_heap)[1])

        return res

# Note: Make sure to push onto heap (frequency, value) so heap can use frequency to evaluate
# Time: O(n logk) -> Have to go through the whole input array to build frequency, and logk pop
# Space: O(n + k) -> Have to build a whole dictionary if every number is unique and pop K times