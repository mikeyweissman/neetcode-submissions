# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        self.res = True

        if not root:
            return True
        
        def height(root):

            if not root:
                return 0 

            l = height(root.left)
            r = height(root.right)

            if abs(l-r) > 1:
                self.res = False

            return 1 + max(l,r)


        height(root)
        return self.res
            
