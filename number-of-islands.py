# https://leetcode.com/problems/number-of-islands/

#["1","1","1","1","0"],
#["1","1","0","1","0"],
#["1","1","0","0","0"],
#["0","0","0","0","0"]



from typing import List
from typing import Set

def pos2geo(x: int, y: int) -> int:
    return x * 1000 + y

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islandCount = 0
        island: Set[int] = set()
        # islands = []

        for x in range(len(grid)):
            for y in range(len(grid[x])):
                if grid[x][y] == "1" and self.isNewIsland(pos2geo(x,y), island):
                    # print("x,y", x,y)
                    self.exploreIsland(grid, island, x,y)
                    islandCount += 1
                    # islands.append(island)
                    
        return islandCount
    
    def isNewIsland(self, geo: int, islands: Set[int]) -> True:
        if geo in islands:
            return False

        return True


    def exploreIsland(self, grid: List[List[str]], island: Set[int], x: int, y: int):
        if 0 > x or x > len(grid) -1 or 0 > y or y > len(grid[x]) -1:
            return

        if grid[x][y] == "0":
            return

        if pos2geo(x, y) in island:
            return

        island.add(pos2geo(x, y))

        self.exploreIsland(grid, island, x, y - 1)
        self.exploreIsland(grid, island, x - 1, y)
        self.exploreIsland(grid, island, x, y + 1)
        self.exploreIsland(grid, island, x + 1, y)
