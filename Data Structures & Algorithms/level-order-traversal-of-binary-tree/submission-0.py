# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root:
            return []

        queue = deque([root])
        res = []

        while queue:

            lvl_length = len(queue)
            curr_lvl = []

            for _ in range(lvl_length):
                node = queue.popleft()
                curr_lvl.append(node.val)
            
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(curr_lvl)

        
        return res
                


            


        
