"""
https://leetcode.com/problems/sliding-window-maximum/
"""

class Solution:
    def getMax(self, arr):
        maxValue = - 100000000
        index = -1

        print("hello")

        for i in range(len(arr)):
            if maxValue < arr[i]:
                maxValue = arr[i]
                index = i

        return maxValue, index

    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        print(len(nums))
        result = []

        (maxValue, index) = self.getMax(nums[0: k])
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
                (maxValue, index) = self.getMax(nums[i - k + 1: i + 1])
                result.append(maxValue)
                # print("appned", maxValue)
            # print("----")
        


        return result