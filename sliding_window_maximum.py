"""
https://leetcode.com/problems/sliding-window-maximum/
https://leetcode.com/problems/sliding-window-maximum/solutions/237611/simplest-o-n-python-solution-with-explanation/

"""

class Solution:
    def getMax2(self, arr, startIndex, endIndex):
        maxValue = -100000000
        index = -1

        length = endIndex-startIndex
        if (length) < 100:
            for i in range(startIndex, endIndex):
                if maxValue < arr[i]:
                    maxValue = arr[i]
                    index = i

            return maxValue, index
        else:
            leftMaxValue, leftIndex = self.getMax(self, arr, startIndex, length/2)
            rightMaxValue, rightIndex = self.getMax(self, arr, length/2, endIndex)

            if leftMaxValue > rightMaxValue:
                return leftMaxValue, leftIndex
            else: 
                return rightMaxValue, rightIndex + length/2
            
    def getMax(self, arr, startIndex, endIndex):
        maxValue = -100000000
        index = -1

        
        for i in range(startIndex, endIndex):
            if maxValue < arr[i]:
                maxValue = arr[i]
                index = i

        return maxValue, index

            
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        print(len(nums))
        result = []

        (maxValue, index) = self.getMax(nums, 0, k)
        result.append(maxValue)

        for i in range(k, len(nums)):
            if i - k + 1 <= index and index <= i and maxValue > nums[i]:
                # print("nums[i]:", nums[i])
                # print("check range 1: ", nums[i - k + 1: i + 1])
                # print("appned", maxValue)
                result.append(maxValue)
            elif i - k + 1 <= index and index <= i and maxValue < nums[i]:
                # print("nums[i]:", nums[i])
                # print("check range 2: ", nums[i - k + 1: i + 1])
                maxValue = nums[i]
                index = i
                result.append(maxValue)
                # print("appned", maxValue)
            elif index < i:
                # print("nums[i]:", nums[i])
                # print("check range 3: ", nums[i - k + 1: i + 1])
                (maxValue, index) = self.getMax(nums, i - k + 1,  i + 1)
                result.append(maxValue)
                # print("appned", maxValue)
            # print("----")
        
        return result