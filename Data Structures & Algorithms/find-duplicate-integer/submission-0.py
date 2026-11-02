class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Linkedlist problem : Cycle detection, cycle mean the starting of the cycle is the dupplicate
        # Floyd Algorithm: fast and slow pointer, when fast = slow , put another slow at the beginning
        #                   then move both slow by 1 until they meet, then that's the start of the cycle

        # 1) Have a slow and fast pointer and move them until they find the intersection 
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        # 2) Have another slow pointer at the begining, then move until both slow pointers meet
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow
        