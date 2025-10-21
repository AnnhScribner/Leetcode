
from typing import List

"""
NOTE: There is a way with Map to make this 
a runtime complexity of O(N)
"""
class Solution:
    """
    Here i compere all my numbers in my array until i find the solution
    O(N^2) -> time complexity
    O(1) -> space complexity
    """
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        list_to_be_returned = []
        for i in range(0, len(nums)):
            for j in range(i + 1,len(nums)):
                if nums[i] + nums[j] == target:
                    list_to_be_returned.append(i)
                    list_to_be_returned.append(j)
                    return list_to_be_returned
        return []
    

s = Solution()

print(s.twoSum([2, 7, 11, 15], 9))   # Expected: [0, 1]
print(s.twoSum([3, 2, 4], 6))        # Expected: [1, 2]
print(s.twoSum([3, 3], 6))           # Expected: [0, 1]
print(s.twoSum([1, 5, 3, 7, 9], 10)) # Expected: [0, 4]
print(s.twoSum([1, 2, 3], 7))        # Expected: []  (no valid pair)
print(s.twoSum([0, 4, 3, 0], 0))     # Expected: [0, 3]
