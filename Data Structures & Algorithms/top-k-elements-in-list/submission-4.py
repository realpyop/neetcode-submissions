class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 1) Create a frequency hashmap to count the freq of elements
        freq = {}
        for num in nums:
            freq[num] = 1 + freq.get(num, 0)
        
        # 2) Use MINHEAP to pop the least freq elements from the top
        heap = []
        for num in freq.keys():
            heapq.heappush(heap, (freq[num], num))
            if len(heap) > k:
                heapq.heappop(heap)
        
        # 3) Build Result of size K
        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res

# Note: Make sure to push onto heap (frequency, value) so heap can use frequency to evaluate
# Time: O(n logk) -> Have to go through the whole input array to build frequency, and logk pop
# Space: O(n + k) -> Have to build a whole dictionary if every number is unique and pop K times