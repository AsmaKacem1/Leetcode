class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        matrix[:] = zip(*matrix[::-1])
        """
        Do not return anything, modify matrix in-place instead.
        """
        