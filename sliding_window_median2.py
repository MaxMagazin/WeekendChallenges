"""
https://leetcode.com/problems/sliding-window-median/
"""
def getMedian(arr: list[int]):
    arrLength = len(arr)
    halfArr = (int) (arrLength / 2)

    if arrLength % 2 == 0:
        return (arr[halfArr - 1] + arr[halfArr])/2
    else:
        return arr[halfArr]


class Solution:
    def medianSlidingWindow(self, nums: list[int], k: int) -> list[float]:
        result = []
        array = nums[0:k]
        array.sort()

        result.append(getMedian(array))

        for i in range(k,len(nums)):    
            array.remove(nums[i-k])
            array.append(nums[i])
            array.sort()
            result.append(getMedian(array))
        return result


s = Solution()
print(s.medianSlidingWindow([1,4,2,3], 4))
