class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # First binary search to find row
        first, last = 0, len(matrix) - 1
        index = 0
        while first <= last:
            mid = (last + first) // 2
            if matrix[mid][0] > target:
                last = mid - 1
            elif matrix[mid][-1] < target:
                first = mid + 1
            else:
                index = mid
                break
        
        # Second binary serach to find the col of the row
        left, right = 0, len(matrix[index]) - 1
        while left <= right:
            mid = (right + left) // 2
            if matrix[index][mid] == target:
                return True
            elif matrix[index][mid] > target:
                right = mid - 1
            elif matrix[index][mid] < target:
                left = mid + 1 
        
        return False