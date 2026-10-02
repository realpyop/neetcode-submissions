class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        total = len(nums1) + len(nums2)
        half = total // 2

        # Run binary search on smaller array
        if len(B) < len(A):
            A, B = B, A
        l, r = 0, len(A) - 1
        while True:
            mid = (l + r) // 2      # A midpoint
            j = half - mid - 2      # index of B
        
            Aleft = A[mid] if mid >= 0 else float("-infinity")
            Aright = A[mid+1] if mid+1 < len(A) else float("infinity")
            Bleft = B[j] if j >= 0 else float("-infinity")
            Bright = B[j+1] if j+1 < len(B) else float("infinity")
        
            # Correct partition
            if Aleft <= Bright and Bleft <= Aright:
                # odd
                if total % 2:
                    return min(Aright, Bright)
                # even
                else:
                    return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            elif Aleft > Bright:
                r = mid - 1
            else:
                l = mid + 1

        