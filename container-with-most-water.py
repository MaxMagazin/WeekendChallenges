#https://leetcode.com/problems/container-with-most-water/description/

from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        left = 0
        right = len(height)-1
        maxVolume = 0

        selectedLeft = 0
        selectedRight = 0

        while left < right:

            volume = self.getVolume(height, left, right)

            if volume > maxVolume:
                maxVolume = volume
                selectedLeft = left
                selectedRight = right


            if height[left] > height[right]:
                right = right - 1
            else:
                left = left +1
            
        return maxVolume

    def getVolume(self, height: List[int], left: int, right: int) -> int:
        return min(height[left], height[right]) * (right - left)



s = Solution()
                #   0 1 2 3 4 5 6 7 8 9
result = s.maxArea([1,8,6,2,100,100,8,3,7])
print(result)