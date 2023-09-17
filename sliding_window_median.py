"""
https://leetcode.com/problems/sliding-window-median/
"""

from typing import List

class Node:
    next = None
    index = -1
    value = 0

    def __init__(self, next, index: int, value: int):
        self.next = next
        self.index = index
        self.value = value

    def __str__(self):
        return f"Node(i: {self.index}, v: {self.value})"

class DL:
    head: Node = None
    size: int = 0

    def __init__(self, size: int):
        self.size = size

    def remove(self, index: int):
        node = self.head        
        prevNode = None
        
        while node.next != None:
            if node.index == index:
                #delete
                if prevNode == None:
                    self.head = node.next
                else:
                    prevNode.next = node.next

            prevNode = node
            node = node.next
    
    def insert(self, index: int, value: int):
        newNode = Node(next=None, index=index, value=value)

        if self.head == None:
            self.head = newNode
            #print(f"was empty, added: {self.head}, {self.tail}")
        else:
            if value <= self.head.value:
                newNode.next = self.head
                self.head = newNode
            else:
                node = self.head
                
                while value >= node.value and node.next != None and value > node.next.value:
                    node = node.next

                if node.next == None:
                    node.next = newNode
                else:
                    newNode.next = node.next
                    node.next = newNode

            print(f"was NOT empty, head: {self.head}")

    def getMedian(self):
        target = self.head

        for i in range((int) ((self.size - 1) / 2)):
            target = target.next
            
        if self.size % 2 == 0:
            return (target.value + target.next.value)/2
        else:
            return target.value

    def __str__(self):
        result = ""
        node = self.head
        while node != None:
            result = result + f"{node}" + "->"
            node = node.next

        return result

class Solution:
    def medianSlidingWindow(self, nums: list[int], k: int) -> list[float]:
        dl = DL(k)
        result = []

        for i in range(len(nums)):    
            dl.insert(i, nums[i])

            if i >= k-1:
                result.append(dl.getMedian())
                dl.remove(i-k)
            
            print(dl)
            
        return result            

        # return [0.1]


s = Solution()
print(s.medianSlidingWindow([1,3,-1,-3,5,3], 3))
