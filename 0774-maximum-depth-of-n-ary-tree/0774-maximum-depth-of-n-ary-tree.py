class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        deque = collections.deque()
        deque.append(root)
        result = 0
        while deque:
            result += 1
            for i in range(len(deque)):
                node = deque.popleft() 
                if node.children:
                    deque.extend(node.children)
        return result
