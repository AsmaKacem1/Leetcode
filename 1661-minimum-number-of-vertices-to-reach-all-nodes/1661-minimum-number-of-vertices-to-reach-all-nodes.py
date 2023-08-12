class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        result=set()
        dist=set()
        for items in edges:
            dist.add(items[1])
        for items in edges:
            if items[0] not in dist:
                result.add(items[0])
        return result
