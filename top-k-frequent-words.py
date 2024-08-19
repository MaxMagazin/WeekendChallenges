# https://leetcode.com/problems/top-k-frequent-words/

from typing import List

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:

        wordsMap = {}

        for word in words:
            if word not in wordsMap:
                wordsMap[word] = 1
            else:
                existed = wordsMap[word]
                wordsMap[word] += 1
        
        print("wordsMap:", wordsMap)

        reversed = {}
        for key,value in wordsMap.items():
            if value not in reversed:
                valueRepeatedWords = [key]
                reversed[value] = valueRepeatedWords
            else:
                valueRepeatedWords = reversed[value]
                valueRepeatedWords.append(key)


        print("reversed:", reversed)

        output = []
        for n in sorted(reversed.keys(), reverse=True):
            if len(output) >= k:
                break
            
            output.append(reversed[n].sort())
        
        return output