# https://leetcode.com/problems/group-anagrams/ 

from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        anagramMap = {}
        for str in strs:
            sortedStr = ''.join(sorted(str))

            if sortedStr not in anagramMap:
                anagramMap[sortedStr] = [str]
            else:
                anagramMap[sortedStr].append(str)

        result = []
        for key in anagramMap:
            result.append(anagramMap[key])

        return result

