# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        if not root:
            return 0

        queue = deque([(root,float('-inf'))])
        res = 0

        while queue:

            node, maxVal = queue.popleft()

            if node.val >= maxVal:
                res += 1
                
                if node.left:
                    queue.append([node.left,node.val])
                
                if node.right:
                    queue.append([node.right,node.val])
                
            
            else:
                    if node.left:
                        queue.append([node.left,maxVal])
                
                    if node.right:
                        queue.append([node.right,maxVal])

        
        return res
            
                
