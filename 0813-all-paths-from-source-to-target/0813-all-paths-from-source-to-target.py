from typing import List
import collections

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n=len(graph)
        def dfs(i,path,result):
            if i==n-1:
                result.append(path)
                return
            for neighbor in graph[i]:
                dfs(neighbor,path+[neighbor],result)
        result=[]
        dfs(0,[0],result)
        return result
