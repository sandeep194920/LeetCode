# User function Template for python3

from typing import List
from queue import Queue


class Solution:
    # Function to return Breadth First Traversal of given graph.
    def bfsOfGraph(self, V: int, adj: List[List[int]]) -> List[int]:
        # code here
        q, visited_arr = [0], [0] * V
        visited_arr[0] = 1
        bfs = []

        while len(q) > 0:
            el = q.pop(0)
            neighbours = adj[el]
            bfs.append(el)
            for nbr in neighbours:
                if visited_arr[nbr] == 0:
                    visited_arr[nbr] = 1
                    q.append(nbr)

        return bfs


result = Solution().bfsOfGraph(V=5, adj=[[1, 2, 3], [], [4], [], []])
print(result)
