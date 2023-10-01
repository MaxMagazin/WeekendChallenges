# https://leetcode.com/problems/merge-intervals/

from typing import List

class Solution:
    def merge(self, intervals):
        inter = sorted(intervals, key=lambda x: x[0])

        output = []

        current = inter[0]
        i = 1

        while i < len(inter):
            if self.intersect(current, inter[i]):
                current = [
                    min(current[0], inter[i][0]),
                    max(current[1], inter[i][1]),
                ]
                i += 1
            else:
                output.append(current)
                current = inter[i]
                i += 1

        output.append(current)

        return output

    def intersect(self, arr1, arr2):
        return (
            self.between(arr1[0], arr2) 
            or self.between(arr1[1], arr2) 
            or self.between(arr2[0], arr1)
        )

    def between(self, value, arr):
        return value >= arr[0] and value <= arr[1]

s = Solution()
print(s.merge([[1,4],[4,5]]))

"""
intervals =
[[2,3],[4,5],[6,7],[8,9],[1,10]]


"""

